from tvDatafeed import TvDatafeed, Interval
import pandas as pd

def get_data(symbol, tf):
    tf_map = {
        '1m': Interval.in_1_minute,
        '5m': Interval.in_5_minute,
        '15m': Interval.in_15_minute,
        '1h': Interval.in_1_hour
    }
    tv = TvDatafeed()
    data = tv.get_hist(symbol=symbol, exchange='FX_IDC', interval=tf_map.get(tf, Interval.in_5_minute), n_bars=100)
    return data.reset_index()