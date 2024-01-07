from datetime import datetime
import json
import asyncio
from unicorn_binance_websocket_api import BinanceWebSocketApiManager

from config import Config, BINANCE_LICENSE_TOKEN, BINANCE_API_SECRET
from utils.logger import get_logger
from kafka import KafkaProducer


class DataCollector():
    def __init__(self) -> None:
        self.binance_client = BinanceWebSocketApiManager(
            lucit_api_secret=BINANCE_API_SECRET,
            lucit_license_token=BINANCE_LICENSE_TOKEN
        )
        self.flag_month = {}
        self.flag_hour = {}

        def serializer(message):
            return json.dumps(message).encode('utf-8')
        self.producer = KafkaProducer(bootstrap_servers=['localhost:19092', 'localhost:29092', 'localhost:39092'],
                                      value_serializer=serializer)
        self.logger = get_logger("Data collector", Config.LOG_FILE)

    def message_handler(self, message: str) -> None:
        # start = datetime.now()
        json_result = json.loads(message)
        if "result" in json_result and not json_result["result"]:
            return

        json_result = json_result["data"]["k"]
        symbol = json_result["s"]
        if json_result["i"] == "1M" and self.flag_month.get(symbol, False):
            self.producer.send(
                Config.KLINE_MONTH_TOPIC, json_result).add_callback(self.on_send_success).add_errback(self.on_send_error)
            self.flag_month[symbol] = False
        # if this result is end of hour, push data hour
        if json_result["i"] == "1h" and json_result["x"]:
            self.producer.send(
                Config.KLINE_HOUR_TOPIC, json_result).add_callback(self.on_send_success).add_errback(self.on_send_error)
            self.flag_hour[symbol] = True
        elif json_result["x"]:
            self.producer.send(
                Config.KLINE_MINUTES_TOPIC, json_result).add_callback(self.on_send_success).add_errback(self.on_send_error)
            # if this result is end of hour, set flag to send month price info
            if self.flag_hour.get(symbol, False):
                self.flag_month[symbol] = True
                self.flag_hour[symbol] = False
            # end = datetime.now()
            # print((end-start).total_seconds() * 1000)

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
            # self.test()
        except Exception as e:
            self.logger.error(f"{e}")
            self.stop()

    def stop(self) -> None:
        self.logger.info("Stop collecting data")
        self.producer.flush()
        self.binance_client.stop_manager_with_all_streams()
