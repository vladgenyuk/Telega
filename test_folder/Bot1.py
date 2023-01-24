import requests
from Bot2.Bot_first.config import BOT_TOKEN

API_link = 'https://api.telegram.org/bot' + BOT_TOKEN + '/'

update = requests.get(API_link + 'getUpdates').json()

message = update['result'][0]

print(message, end='\n\n')


chat_id = message['message']['chat']['id']
text = message['message']['text']

print(chat_id, text)


sent_message = requests.get(API_link + f'sendMessage?chat_id={chat_id}&text=Пивет, ты написал {text}')