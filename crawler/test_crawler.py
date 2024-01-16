import pytest
import json
from collector import DataCollector
from config import Config

collector = DataCollector()



class TestCrawler:
    def test_send_min_data(self):
        data = {
            "data": {
                "k": {
                    "i": "1m",
                    "x": True,
                    "s": "BTCUSDT"
                }
            },
        }
        assert collector.message_handler(json.dumps(data)) == Config.KLINE_MINUTES_TOPIC

    def test_send_hour_data(self):
        data = {
            "data": {
                "k": {
                    "i": "1h",
                    "x": True,
                    "s": "BTCUSDT"
                }
            },
        }
        assert collector.message_handler(json.dumps(data)) == Config.KLINE_HOUR_TOPIC

    def test_send_mon_data(self):
        data = {
            "data": {
                "k": {
                    "i": "1M",
                    "x": True,
                    "s": "BTCUSDT"
                }
            },
        }
        assert collector.message_handler(json.dumps(data)) == Config.KLINE_MONTH_TOPIC
