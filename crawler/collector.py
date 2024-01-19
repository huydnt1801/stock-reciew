import json
import asyncio
from unicorn_binance_websocket_api import BinanceWebSocketApiManager

from config import Config, BINANCE_LICENSE_TOKEN, BINANCE_API_SECRET
from utils.logger import get_logger
from kafka import KafkaProducer
import pymongo


class DataCollector():
    def __init__(self) -> None:
        self.logger = get_logger("Data collector", Config.LOG_FILE)
        try:
            self.binance_client = BinanceWebSocketApiManager(
                lucit_api_secret=BINANCE_API_SECRET,
                lucit_license_token=BINANCE_LICENSE_TOKEN
            )
        except Exception as e:
            self.logger.info(e)
        client = pymongo.MongoClient(Config.DB_URL)
        self.db = client["crypto_assessment"]
        self.flag_month = {}

        def serializer(message):
            return json.dumps(message).encode('utf-8')
        try:
            print(Config.KAFKA_BROKERS)
            self.producer = KafkaProducer(bootstrap_servers=Config.KAFKA_BROKERS,
                                        value_serializer=serializer)
        except Exception as e:
            self.logger.error(e)

    def message_handler(self, message: str) -> None:
        json_result = json.loads(message)
        if "result" in json_result and not json_result["result"]:
            return

        json_result = json_result["data"]["k"]
        symbol = json_result["s"]
        if json_result["i"] == "1M":
            event_time = self.flag_month.get(symbol, None)
            if event_time:
                collection = self.db[symbol]
                cur = collection.find_one({"event_time": event_time})
                if cur is not None:
                    try:
                        self.producer.send(
                            Config.KLINE_MONTH_TOPIC, json_result).add_callback(self.on_send_success).add_errback(self.on_send_error)
                    except Exception as e:
                        self.logger.error(e)
                    self.flag_month[symbol] = 0
            return Config.KLINE_MONTH_TOPIC
        # if this result is end of hour, push data hour
        elif json_result["i"] == "1h":
            if json_result["x"]:
                try:
                    self.producer.send(
                        Config.KLINE_HOUR_TOPIC, json_result).add_callback(self.on_send_success).add_errback(self.on_send_error)
                    self.flag_month[symbol] = json_result['t']
                except Exception as e:
                    self.logger.error(e)
            return Config.KLINE_HOUR_TOPIC
        elif json_result["i"] == "1m" and json_result["x"]:
            try:
                self.producer.send(
                    Config.KLINE_MINUTES_TOPIC, json_result).add_callback(self.on_send_success).add_errback(self.on_send_error)
            except Exception as e:
                self.logger.error(e)
            return Config.KLINE_MINUTES_TOPIC
        return "END"

    async def collect_data(self) -> None:
        self.binance_client.create_stream(
            channels=Config.SUBCRIBE_CHANNELS,
            markets=Config.SYMBOL_LIST,
            process_stream_data=self.message_handler
        )
        while True:
            await asyncio.sleep(1)

    def on_send_success(self, record_metadata):
        info = {
            "topic": record_metadata.topic,
            "partition": record_metadata.partition,
            "offset": record_metadata.offset,
        }
        self.logger.info("Success send msg: " + str(info))

    def on_send_error(self, excp):
        self.logger.error("Failed send msg: " + str(excp))

    def start(self) -> None:
        self.logger.info("Start collect data")
        try:
            asyncio.run(self.collect_data())
            # self.message_handler(json.dumps({"data": {"k": {"t": 1696809600000, "T": 1697414399999, "s": "BTCUSDT", "i": "1M", "f": 69915457, "L": 69937421, "o": "0.00000316", "c": "0.00000317", "h": "0.00000324", "l": "0.00000311", "v": "65229990.00000000", "n": 21965, "x": True, "q": "206.97094079", "V": "32330456.00000000", "Q": "102.73648818", "B": "0"}}}))
        except Exception as e:
            self.logger.error(f"{e}")
            self.stop()

    def stop(self) -> None:
        try:
            self.logger.info("Stop collecting data")
            self.producer.flush()
            self.binance_client.stop_manager_with_all_streams()
        except Exception as e:
            self.logger.error(e)
