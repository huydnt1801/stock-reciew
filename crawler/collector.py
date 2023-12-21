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
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                                      value_serializer=serializer)
        self.logger = get_logger("Data collector", Config.LOG_FILE)

    def message_handler(self, message: str) -> None:
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

    def test(self):
        data = [{'open_time': 1701875880000, 'end_time': 1701875939999, 'symbol': 'BTCUSDT', 'interval': '1m', 'first_trade_id': 3309865817, 'last_trade_id': 3309869470, 'open': 43960.01, 'close': 43934.0, 'high': 43984.0, 'low': 43911.12, 'volume': 86.5853, 'number_of_trade': 3654, 'is_closed': True, 'completed_trade_amount': 3805800.4703166, 'taker_completed_trade_volume': 38.68763, 'taker_trade_amount': 1700471.5094255}, {'open_time': 1701875940000, 'end_time': 1701875999999, 'symbol': 'BTCUSDT', 'interval': '1m', 'first_trade_id': 3309869471, 'last_trade_id': 3309871492, 'open': 43933.99, 'close': 43952.48, 'high': 43953.52, 'low': 43912.7, 'volume': 41.18121, 'number_of_trade': 2022, 'is_closed': True, 'completed_trade_amount': 1809492.9389192, 'taker_completed_trade_volume': 23.55217, 'taker_trade_amount': 1034841.5011886}, {'open_time': 1701876000000, 'end_time': 1701876059999, 'symbol': 'BTCUSDT', 'interval': '1m', 'first_trade_id': 3309871493, 'last_trade_id': 3309873232, 'open': 43952.48, 'close': 43998.2, 'high': 43998.2, 'low': 43951.64, 'volume': 26.41537, 'number_of_trade': 1740, 'is_closed': True, 'completed_trade_amount': 1161339.1036854, 'taker_completed_trade_volume': 17.25675, 'taker_trade_amount': 758710.4420413}, {'open_time': 1701876060000, 'end_time': 1701876119999, 'symbol': 'BTCUSDT', 'interval': '1m', 'first_trade_id': 3309873233, 'last_trade_id': 3309874627, 'open': 43998.19, 'close': 43954.0, 'high': 44009.18, 'low': 43953.82, 'volume': 19.84934, 'number_of_trade': 1395, 'is_closed': True, 'completed_trade_amount': 873126.1667547, 'taker_completed_trade_volume': 8.58973, 'taker_trade_amount': 377814.4833869}, {'open_time': 1701876120000, 'end_time': 1701876179999, 'symbol': 'BTCUSDT', 'interval': '1m', 'first_trade_id': 3309874628, 'last_trade_id': 3309875919, 'open': 43953.99, 'close': 43977.09, 'high': 43977.1, 'low': 43941.11, 'volume': 22.88148, 'number_of_trade': 1292, 'is_closed': True, 'completed_trade_amount': 1005806.6687608, 'taker_completed_trade_volume': 10.20199, 'taker_trade_amount': 448480.6672824}, {'open_time': 1701876180000, 'end_time': 1701876239999, 'symbol': 'BTCUSDT', 'interval': '1m', 'first_trade_id': 3309875920, 'last_trade_id': 3309877122, 'open': 43977.09, 'close': 43988.89, 'high': 44000.0, 'low': 43977.09, 'volume': 36.00877, 'number_of_trade': 1203, 'is_closed': True, 'completed_trade_amount': 1583896.3640337, 'taker_completed_trade_volume': 19.05992, 'taker_trade_amount': 838292.7036735}, {'open_time': 1701876240000, 'end_time': 1701876299999, 'symbol': 'BTCUSDT', 'interval': '1m', 'first_trade_id': 3309877123, 'last_trade_id': 3309878255, 'open': 43988.9, 'close': 43951.09, 'high': 44004.0, 'low': 43939.23, 'volume': 21.77597, 'number_of_trade': 1133, 'is_closed': True, 'completed_trade_amount': 957478.7926788, 'taker_completed_trade_volume': 11.26903, 'taker_trade_amount': 495512.0878469}, {'open_time': 1701876300000, 'end_time': 1701876359999, 'symbol': 'BTCUSDT', 'interval': '1m', 'first_trade_id': 3309878256, 'last_trade_id': 3309879745, 'open': 43951.1, 'close': 43920.01, 'high': 43971.1, 'low': 43920.0, 'volume': 36.95362, 'number_of_trade': 1490, 'is_closed': True, 'completed_trade_amount': 1623999.7502573, 'taker_completed_trade_volume': 12.53516, 'taker_trade_amount': 550866.217744}, {'open_time': 1701876360000, 'end_time': 1701876419999, 'symbol': 'BTCUSDT', 'interval': '1m', 'first_trade_id': 3309879746, 'last_trade_id': 3309882416, 'open': 43920.01, 'close': 43889.12, 'high': 43944.01, 'low': 43874.71, 'volume': 77.08939, 'number_of_trade': 2671, 'is_closed': True, 'completed_trade_amount': 3384513.0286803, 'taker_completed_trade_volume': 32.60553, 'taker_trade_amount': 1431516.5128077}, {'open_time': 1701876420000, 'end_time': 1701876479999, 'symbol': 'BTCUSDT', 'interval': '1m', 'first_trade_id': 3309882417, 'last_trade_id': 3309883816, 'open': 43889.12, 'close': 43878.37, 'high': 43917.84, 'low': 43878.37, 'volume': 31.30969, 'number_of_trade': 1400, 'is_closed': True, 'completed_trade_amount': 1374583.3256044, 'taker_completed_trade_volume': 12.46757, 'taker_trade_amount': 547331.3620182}, {'open_time': 1701876480000, 'end_time': 1701876539999, 'symbol': 'BTCUSDT', 'interval': '1m', 'first_trade_id': 3309883817, 'last_trade_id': 3309885941, 'open': 43878.38, 'close': 43887.05, 'high': 43900.0, 'low': 43858.28, 'volume': 53.78625, 'number_of_trade': 2125, 'is_closed': True, 'completed_trade_amount': 2360247.5180636, 'taker_completed_trade_volume': 25.22499, 'taker_trade_amount': 1106913.946586}, {'open_time': 1701876540000, 'end_time': 1701876599999, 'symbol': 'BTCUSDT', 'interval': '1m', 'first_trade_id': 3309885942, 'last_trade_id': 3309887415, 'open': 43887.05, 'close': 43925.84, 'high': 43925.85, 'low': 43880.01, 'volume': 38.09635, 'number_of_trade': 1474, 'is_closed': True, 'completed_trade_amount': 1672501.373863, 'taker_completed_trade_volume': 24.68556, 'taker_trade_amount': 1083779.7752911}, {'open_time': 1701876600000, 'end_time': 1701876659999, 'symbol': 'BTCUSDT', 'interval': '1m', 'first_trade_id': 3309887416, 'last_trade_id': 3309888664, 'open': 43925.84, 'close': 43945.98, 'high': 43947.73, 'low': 43916.0, 'volume': 34.8747, 'number_of_trade': 1249, 'is_closed': True, 'completed_trade_amount': 1532170.8913245, 'taker_completed_trade_volume': 19.32865, 'taker_trade_amount': 849135.1647098}, {'open_time': 1701876660000, 'end_time': 1701876719999, 'symbol': 'BTCUSDT', 'interval': '1m', 'first_trade_id': 3309888665, 'last_trade_id': 3309890000, 'open': 43945.98, 'close': 43942.99, 'high': 43982.0, 'low': 43942.99, 'volume': 25.76795, 'number_of_trade': 1336, 'is_closed': True, 'completed_trade_amount': 1132750.9949939, 'taker_completed_trade_volume': 14.19556, 'taker_trade_amount': 624016.3360637}, {'open_time': 1701876720000, 'end_time': 1701876779999, 'symbol': 'BTCUSDT', 'interval': '1m', 'first_trade_id': 3309890001, 'last_trade_id': 3309891476, 'open': 43942.99, 'close': 43921.95, 'high': 43946.05, 'low': 43900.04, 'volume': 58.02999, 'number_of_trade': 1476, 'is_closed': True, 'completed_trade_amount': 2549018.2952577, 'taker_completed_trade_volume': 21.64066, 'taker_trade_amount': 950361.2990448}, {
            'open_time': 1701876780000, 'end_time': 1701876839999, 'symbol': 'BTCUSDT', 'interval': '1m', 'first_trade_id': 3309891477, 'last_trade_id': 3309892798, 'open': 43921.95, 'close': 43909.83, 'high': 43945.83, 'low': 43909.83, 'volume': 25.4311, 'number_of_trade': 1322, 'is_closed': True, 'completed_trade_amount': 1117239.6042464, 'taker_completed_trade_volume': 10.3909, 'taker_trade_amount': 456470.6187727}, {'open_time': 1701876840000, 'end_time': 1701876899999, 'symbol': 'BTCUSDT', 'interval': '1m', 'first_trade_id': 3309892799, 'last_trade_id': 3309894275, 'open': 43909.84, 'close': 43873.97, 'high': 43909.84, 'low': 43865.64, 'volume': 47.08534, 'number_of_trade': 1477, 'is_closed': True, 'completed_trade_amount': 2066192.4356869, 'taker_completed_trade_volume': 14.77973, 'taker_trade_amount': 648477.2502037}, {'open_time': 1701876900000, 'end_time': 1701876959999, 'symbol': 'BTCUSDT', 'interval': '1m', 'first_trade_id': 3309894276, 'last_trade_id': 3309895863, 'open': 43873.97, 'close': 43919.5, 'high': 43919.51, 'low': 43865.12, 'volume': 38.8532, 'number_of_trade': 1588, 'is_closed': True, 'completed_trade_amount': 1704887.2492971, 'taker_completed_trade_volume': 14.0506, 'taker_trade_amount': 616537.441141}, {'open_time': 1701876960000, 'end_time': 1701877019999, 'symbol': 'BTCUSDT', 'interval': '1m', 'first_trade_id': 3309895864, 'last_trade_id': 3309897257, 'open': 43919.5, 'close': 43870.15, 'high': 43926.0, 'low': 43870.14, 'volume': 31.84572, 'number_of_trade': 1394, 'is_closed': True, 'completed_trade_amount': 1398404.2746919, 'taker_completed_trade_volume': 20.31975, 'taker_trade_amount': 892384.646397}, {'open_time': 1701877020000, 'end_time': 1701877079999, 'symbol': 'BTCUSDT', 'interval': '1m', 'first_trade_id': 3309897258, 'last_trade_id': 3309900799, 'open': 43870.14, 'close': 43819.12, 'high': 43876.01, 'low': 43804.0, 'volume': 122.92072, 'number_of_trade': 3542, 'is_closed': True, 'completed_trade_amount': 5389527.633857, 'taker_completed_trade_volume': 48.28751, 'taker_trade_amount': 2116793.5609218}, {'open_time': 1701877080000, 'end_time': 1701877139999, 'symbol': 'BTCUSDT', 'interval': '1m', 'first_trade_id': 3309900800, 'last_trade_id': 3309902528, 'open': 43819.11, 'close': 43807.95, 'high': 43855.1, 'low': 43807.95, 'volume': 51.78147, 'number_of_trade': 1729, 'is_closed': True, 'completed_trade_amount': 2269696.6907478, 'taker_completed_trade_volume': 22.07848, 'taker_trade_amount': 967780.1613843}, {'open_time': 1701877140000, 'end_time': 1701877199999, 'symbol': 'BTCUSDT', 'interval': '1m', 'first_trade_id': 3309902529, 'last_trade_id': 3309904056, 'open': 43807.95, 'close': 43846.01, 'high': 43852.31, 'low': 43807.46, 'volume': 39.43225, 'number_of_trade': 1528, 'is_closed': True, 'completed_trade_amount': 1728477.6420319, 'taker_completed_trade_volume': 23.20715, 'taker_trade_amount': 1017258.0567472}, {'open_time': 1701877200000, 'end_time': 1701877259999, 'symbol': 'BTCUSDT', 'interval': '1m', 'first_trade_id': 3309904057, 'last_trade_id': 3309905431, 'open': 43846.01, 'close': 43859.57, 'high': 43871.41, 'low': 43846.0, 'volume': 50.27108, 'number_of_trade': 1375, 'is_closed': True, 'completed_trade_amount': 2204853.5814153, 'taker_completed_trade_volume': 16.20184, 'taker_trade_amount': 710541.463906}, {'open_time': 1701877260000, 'end_time': 1701877319999, 'symbol': 'BTCUSDT', 'interval': '1m', 'first_trade_id': 3309905432, 'last_trade_id': 3309907769, 'open': 43859.58, 'close': 43890.6, 'high': 43915.59, 'low': 43856.43, 'volume': 101.79549, 'number_of_trade': 2338, 'is_closed': True, 'completed_trade_amount': 4467404.3292392, 'taker_completed_trade_volume': 48.6754, 'taker_trade_amount': 2136263.1309137}, {'open_time': 1701877320000, 'end_time': 1701877379999, 'symbol': 'BTCUSDT', 'interval': '1m', 'first_trade_id': 3309907770, 'last_trade_id': 3309909599, 'open': 43890.6, 'close': 43944.73, 'high': 43968.0, 'low': 43890.6, 'volume': 48.16225, 'number_of_trade': 1830, 'is_closed': True, 'completed_trade_amount': 2115810.371911, 'taker_completed_trade_volume': 28.59526, 'taker_trade_amount': 1255886.4114424}, {'open_time': 1701877380000, 'end_time': 1701877439999, 'symbol': 'BTCUSDT', 'interval': '1m', 'first_trade_id': 3309909600, 'last_trade_id': 3309911083, 'open': 43944.73, 'close': 43908.24, 'high': 43944.74, 'low': 43908.24, 'volume': 52.23316, 'number_of_trade': 1484, 'is_closed': True, 'completed_trade_amount': 2294324.0093745, 'taker_completed_trade_volume': 30.77474, 'taker_trade_amount': 1351736.9397422}, {'open_time': 1701877440000, 'end_time': 1701877499999, 'symbol': 'BTCUSDT', 'interval': '1m', 'first_trade_id': 3309911084, 'last_trade_id': 3309912500, 'open': 43908.24, 'close': 43836.02, 'high': 43908.25, 'low': 43835.2, 'volume': 32.79501, 'number_of_trade': 1417, 'is_closed': True, 'completed_trade_amount': 1438547.4404388, 'taker_completed_trade_volume': 7.15863, 'taker_trade_amount': 314051.2647369}, {'open_time': 1701877500000, 'end_time': 1701877559999, 'symbol': 'BTCUSDT', 'interval': '1m', 'first_trade_id': 3309912501, 'last_trade_id': 3309915379, 'open': 43836.01, 'close': 43840.0, 'high': 43850.0, 'low': 43783.38, 'volume': 96.5617, 'number_of_trade': 2879, 'is_closed': True, 'completed_trade_amount': 4230983.7130449, 'taker_completed_trade_volume': 45.93562, 'taker_trade_amount': 2013091.1807151}, {'open_time': 1701877560000, 'end_time': 1701877619999, 'symbol': 'BTCUSDT', 'interval': '1m', 'first_trade_id': 3309915380, 'last_trade_id': 3309917187, 'open': 43839.99, 'close': 43906.0, 'high': 43906.0, 'low': 43823.87, 'volume': 45.20647, 'number_of_trade': 1808, 'is_closed': True, 'completed_trade_amount': 1983059.8754808, 'taker_completed_trade_volume': 23.37215, 'taker_trade_amount': 1025356.0988405}, {'open_time': 1701877620000, 'end_time': 1701877679999, 'symbol': 'BTCUSDT', 'interval': '1m', 'first_trade_id': 3309917188, 'last_trade_id': 3309918810, 'open': 43906.0, 'close': 43860.01, 'high': 43919.51, 'low': 43860.0, 'volume': 39.69991, 'number_of_trade': 1623, 'is_closed': True, 'completed_trade_amount': 1742512.5124768, 'taker_completed_trade_volume': 13.97896, 'taker_trade_amount': 613456.980836}]
        for d in data:
            self.producer.send(
                Config.KLINES_KAFKA_TOPIC, d).add_callback(self.on_send_success).add_errback(self.on_send_error)

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
