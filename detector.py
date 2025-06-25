def check_zones(df):
    last = df.iloc[-1]
    prev = df.iloc[-2]

    if last['high'] > prev['high'] and last['low'] > prev['low']:
        return {
            'pair': 'XAUUSD',
            'zone': 'BOS',
            'signal': 'BUY',
            'entry': round(last['close'], 2),
            'tp1': round(last['close'] + 3, 2),
            'tp2': round(last['close'] + 6, 2),
            'tp_max': round(last['close'] + 10, 2),
            'sl': round(last['close'] - 5, 2)
        }
    return None