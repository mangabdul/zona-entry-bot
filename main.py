from fetcher import get_data
from detector import check_zones
from bot import send_signal
import time

symbols = [("XAUUSD", "5m"), ("BTCUSDT", "5m")]

while True:
    for symbol, tf in symbols:
        df = get_data(symbol, tf)
        signal = check_zones(df, symbol)
        if signal:
            send_signal(signal)
    time.sleep(60)