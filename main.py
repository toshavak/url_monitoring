import requests
import pyttsx3
import time
from telegram import Bot

URL = ''
TOKEN = ''

bot = Bot(token=TOKEN)

engine = pyttsx3.init()
engine.setProperty('rate', 200)
engine.setProperty('volume', 1)

url_update = f"https://api.telegram.org/bot .../getUpdates"


def get_chat_ids(update):
    return {chat['message']['chat']['id'] for chat in update['result']}


def get_updates():
    return requests.get(url_update).json()


def all_chats():
    update = get_updates()
    return get_chat_ids(update)


def send_message(chat_id, message):
    requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}")
    time.sleep(.1)


def multy_send(chats, message):
    for chat in chats:
        send_message(chat, message)


try:
    while True:
        response = requests.get(URL)
        text = str(response.status_code)
        message = f'{URL} - status code: {text}'

        if response.status_code != 404:
            engine.say(text)
            engine.runAndWait()

        chats = all_chats()
        multy_send(chats, message)
        print(message)

        time.sleep(5)

except Exception as e:
    text = f'ERROR! Run stopped - {str(e)}'
    chats = all_chats()
    multy_send(chats, text)
    engine.say(text)
    engine.runAndWait()
    time.sleep(.5)
