from fetcher import get_data
from detector import check_zones
from bot import send_signal
import time

while True:
    df = get_data("XAUUSD", "5m")
    signal = check_zones(df)
    if signal:
        send_signal(signal)
    time.sleep(60)  # Cek setiap 1 menit