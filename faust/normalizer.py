import json
KLINES_COLS_NORMALIZED_COLS = {
    "t": {"name": "start_time", "type": "long"},
    "T": {"name": "close_time", "type": "long"},
    "s": {"name": "symbol", "type": "string"},
    "i": {"name": "interval", "type": "string"},
    "f": {"name": "first_trade_id", "type": "long"},
    "L": {"name": "last_trade_id", "type": "long"},
    "o": {"name": "open_price", "type": "double"},
    "c": {"name": "close_price", "type": "double"},
    "h": {"name": "high_price", "type": "double"},
    "l": {"name": "low_price", "type": "double"},
    "v": {"name": "base_asset_vol", "type": "double"},
    "n": {"name": "number_of_trade", "type": "long"},
    "x": {"name": "is_closed", "type": "boolean"},
    "q": {"name": "quote_asset_vol", "type": "double"},
    "V": {"name": "buy_base_asset_vol", "type": "double"},
    "Q": {"name": "buy_quote_asset_vol", "type": "double"}
}


def normalize_data(payload):
    data = json.loads(payload)
    res = {}
    for column, attrs in KLINES_COLS_NORMALIZED_COLS.items():
        res.update({attrs["name"]: data[column]})
    return res
