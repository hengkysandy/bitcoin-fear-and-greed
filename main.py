#0 7 * * * /bin/python3.7 /path/to/main.py
import telebot
import time
import requests
from datetime import datetime

API_KEY = '<TELEGRAM_API_KEY>'
bot = telebot.TeleBot(API_KEY)

message_id = '<YOUR_TELEGRAM_CHANNEL_ID>'

def main():
    req = requests.get('https://api.alternative.me/fng/').json()
    today = datetime.today()
    date_now = str(today.year) + '-' + str(today.month) + '-' + str(today.day)
    status = req['data'][0]['value_classification']
    if status == 'Extreme Fear' or status == 'Extreme Greed': 
        option = 'SELL'
        if status == 'Extreme Fear':
            option = 'BUY'
        msg = 'Market is now on ' + status + ', which can be considered as ' + option + ' opportunity.'
        bot.send_photo(message_id, photo='https://alternative.me/images/fng/crypto-fear-and-greed-index-'+date_now+'.png', caption = msg)


main()