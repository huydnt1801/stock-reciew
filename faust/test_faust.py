import os
import pytest
import pandas as pd
from assessment import Assessment
from indicator import Indicator

data_min = pd.read_csv(f'{os.path.dirname(os.path.realpath(__file__))}/data/BTCUSDT-1m.csv')
data_hour = pd.read_csv(f'{os.path.dirname(os.path.realpath(__file__))}/data/BTCUSDT-1h.csv')
assessment = Assessment(
            "BTCUSDT",  data_min.to_dict(orient="records"), data_hour.to_dict(orient="records")[0], data_hour.to_dict(orient="records")[0])
high, low, cnt_change = assessment.process()

indicator = Indicator(data_hour.to_dict(orient="records")[0:15])
class TestProcessing:
    def test_process_price(self):
        msg = assessment._hour_price()
        assert msg == "\nTrong giờ qua, giá BTCUSDT giảm 0.37% từ 42847.99 xuống 42687.36"
        msg = assessment._price()
        assert msg == "\nTrong giờ qua, giá BTCUSDT cao nhất là: 42890.23 lúc 7:8 và thấp nhất là: 42664.0 lúc 7:46"

    def test_process_volume(self):
        msg = assessment._volume_analysis(high, low)
        assert msg == "\nTừ 7:53 đến 7:56 BTCUSDT tăng 0.13% với volume trung bình cao nhất 33.97/phút\nTừ 7:44 đến 7:49 BTCUSDT giảm 0.16% với volume trung bình cao nhất 20.78/phút"

    def test_change_number(self):
        assert len(high) == 10
        assert len(low) == 10
        assert cnt_change == 20


class TestIndicator:
    def test_mfi(self):
        assert indicator.MFI() == 52.35710216072967

    def test_rsi(self):
        assert indicator.RSI() == 54.78856247070292
