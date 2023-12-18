import json
KLINES_COLS_NORMALIZED_COLS = {
    "t": {"name": "open_time", "type": "long"},
    "T": {"name": "end_time", "type": "long"},
    "s": {"name": "symbol", "type": "string"},
    "i": {"name": "interval", "type": "string"},
    "f": {"name": "first_trade_id", "type": "long"},
    "L": {"name": "last_trade_id", "type": "long"},
    "o": {"name": "open", "type": "double"},
    "c": {"name": "close", "type": "double"},
    "h": {"name": "high", "type": "double"},
    "l": {"name": "low", "type": "double"},
    "v": {"name": "volume", "type": "double"},
    "n": {"name": "number_of_trade", "type": "long"},
    "x": {"name": "is_closed", "type": "boolean"},
    "q": {"name": "completed_trade_amount", "type": "double"},
    "V": {"name": "taker_completed_trade_volume", "type": "double"},
    "Q": {"name": "taker_trade_amount", "type": "double"}
}


def normalize_data(payload):
    data = json.loads(payload)
    res = {}
    for column, attrs in KLINES_COLS_NORMALIZED_COLS.items():
        value = data[column]
        if attrs["type"] == "long":
            value = int(value)
        elif attrs["type"] == "double":
            value = float(value)
        elif attrs["type"] == "boolean":
            value = bool(value)
        elif attrs["type"] == "string":
            value = str(value)
        res.update({attrs["name"]: value})
    return res
