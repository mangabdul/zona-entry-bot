import requests
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("USER_ID")

def send_signal(signal):
    text = f"""📡 Zona Entry Terdeteksi

📍 Pair: {signal['pair']}
📊 Zona: {signal['zone']}
🟢 Sinyal: {signal['signal']}
💰 Entry: {signal['entry']}

🎯 Take Profit:
• TP1: {signal['tp1']}
• TP2: {signal['tp2']}
• TP Max: {signal['tp_max']}

❌ Stop Loss: {signal['sl']}
""" 
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})