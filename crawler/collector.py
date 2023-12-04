import json
import asyncio
from unicorn_binance_websocket_api import BinanceWebSocketApiManager

from config import Config, BINANCE_LICENSE_TOKEN, BINANCE_API_SECRET
from utils.logger import get_logger
from kafka import KafkaProducer


class DataCollector():
    def __init__(self) -> None:
        self.binance_client = BinanceWebSocketApiManager(
            exchange="binance.com",
            lucit_api_secret=BINANCE_API_SECRET,
            lucit_license_token=BINANCE_LICENSE_TOKEN
        )
        def serializer(message):
            return json.dumps(message).encode('utf-8')
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                                      value_serializer=serializer)
        self.url = Config.BINANCE_INFO_URL
        self.logger = get_logger("Data collector", Config.LOG_FILE)

    def message_handler(self, message: str) -> None:
        json_result = json.loads(message)
        if "result" in json_result and not json_result["result"]:
            return

        json_result = json_result["data"]
        if json_result["e"] == Config.KLINES_EVENT_TYPE:
            self.producer.send(
                Config.KLINES_KAFKA_TOPIC, json.dumps(json_result["k"])).add_callback(self.on_send_success).add_errback(self.on_send_error)
            self.producer.poll(0)

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
        except Exception as e:
            self.logger.error(f"{e}")
            print(e)
            self.stop()

    def stop(self) -> None:
        self.logger.info("Stop collecting data")
        self.producer.flush()
        self.binance_client.stop_manager_with_all_streams()
