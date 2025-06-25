def is_bos_up(last, prev):
    return (
        last['high'] > prev['high'] and
        last['low'] > prev['low'] and
        (last['close'] - last['open']) > 0.5
    )

def is_bos_down(last, prev):
    return (
        last['high'] < prev['high'] and
        last['low'] < prev['low'] and
        (prev['open'] - prev['close']) > 0.5
    )

def check_zones(df, pair_name):
    last = df.iloc[-1]
    prev = df.iloc[-2]

    if is_bos_up(last, prev):
        entry = round(last['close'], 2)
        return {
            'pair': pair_name,
            'zone': 'BOS',
            'signal': 'BUY',
            'entry': entry,
            'tp1': round(entry + entry * 0.0015, 2),
            'tp2': round(entry + entry * 0.003, 2),
            'tp_max': round(entry + entry * 0.006, 2),
            'sl': round(entry - entry * 0.003, 2)
        }

    elif is_bos_down(last, prev):
        entry = round(last['close'], 2)
        return {
            'pair': pair_name,
            'zone': 'BOS',
            'signal': 'SELL',
            'entry': entry,
            'tp1': round(entry - entry * 0.0015, 2),
            'tp2': round(entry - entry * 0.003, 2),
            'tp_max': round(entry - entry * 0.006, 2),
            'sl': round(entry + entry * 0.003, 2)
        }

    return None