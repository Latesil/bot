#бот
import telebot
import os
import random
import urllib.request as urllib2
import requests
import time
from flask import Flask,request
from bs4 import BeautifulSoup

mensiratus = 171568889
i_am = 170060564
soider = 75266684
stolen = 167379044

token = os.environ["TOKEN_BOT"]
bot = telebot.TeleBot(token)


WEBHOOK_HOST = 'skipabot.herokuapp.com'
WEBHOOK_URL_PATH = '/bot'
WEBHOOK_PORT = os.environ.get('PORT',5000)
WEBHOOK_LISTEN = '0.0.0.0'


WEBHOOK_URL_BASE = "https://%s/%s"% (WEBHOOK_HOST,WEBHOOK_URL_PATH)

server=Flask(__name__)

#responce for commands
@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id, 'Ничем помочь не могу. Попробуй другую команду.')
#responce for settings
@bot.message_handler(commands=['settings'])
def handle_text(message):
    bot.send_message(message.chat.id, 'Ну и что ты ожидал тут увидеть?')

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', '/settings')
    user_markup.row('/help', '/2ch')
    bot.send_message(message.from_user.id, "Привет, человек. Напиши мне че угодно.", reply_markup=user_markup)
    time.sleep(2)
    bot.send_message(message.from_user.id, "Или можешь ещё спросить что-нибудь. Напиши: окбот (и далее твой вопрос)", reply_markup=user_markup)

#foto from internet
@bot.message_handler(commands=['2ch'])
def from_url(message):
    all_boards = {
        'b':'https://2ch.hk/b/',
        'a':'https://2ch.hk/a/',
        'wp':'https://2ch.hk/wp/',
        'aa':'https://2ch.hk/aa/',
        'e':'https://2ch.hk/e/',
        'po':'https://2ch.hk/po/',
        'ga':'https://2ch.hk/ga/',
    }
    list_urls = []
    time.sleep(0.5)
    bot.send_message(message.chat.id, "Щас, секунду...")
    board = random.choice(list(all_boards.keys()))
    for key, value in all_boards.items():
        if key == board:
            board_url = value
    resp = requests.get(board_url) #all page code
    try:
        resp.raise_for_status()
        plain_text = resp.text #convert all code to string
        soup = BeautifulSoup(plain_text, 'lxml')
        #print(list_urls)
        for img in soup.findAll('a', {'name': 'expandfunc'}):
            link_to_image = img.get('href')
            #add links on threads to list
            if link_to_image is not None and '.webm' not in link_to_image and '.gif' not in link_to_image:
                    list_urls.append('http://2ch.hk' + link_to_image)
        url = random.choice(list_urls)
        time.sleep(2)
        bot.send_photo(message.from_user.id, url)
        time.sleep(2)
        if board == 'ga':
            bot.send_message(message.chat.id, "Петушок, эта картинка была специально для тебя, прямиком из:" + " " + board_url)
        else:
            bot.send_message(message.chat.id, "Хочешь ещё? Жми: /2ch")
    except requests.exceptions.HTTPError:
        list_urls.append('https://2ch.hk/images/monkey_not_found.jpg')
        bot.send_message(message.chat.id, "Сорян, что-то пошло не так. Попробуй снова.")



#responses for message (or from_user.id)
@bot.message_handler(content_types=['text'])
def handle_text(message):
    melody = """Там.. татарам-тара-там...
        татара-тара-там..
        тра-та-тара-тара-там
        ТА-ТА..."""
    notes = {
        'C':'G, Am, F','G':'C, Em, D','D':'G, Hm, A',
        'A':'E, Fm#, D','E':'A, Cm#, H','H':'Gm#, Gb (F#), E',
        'Gb':'Db, Emb, H','F#':'Db, Emb, H','Db':'Bm b, Gb (F#), Ab',
        'C#':'Bm b, Gb (F#), Ab','G#':'Eb, Fm, Db','Ab':'Eb, Fm, Db',
        'Eb':'Bb, Cm, Ab','D#':'Bb, Cm, Ab','Bb':'Gm, Eb, F',
        'A#':'Gm, Eb, F','F':'C, Bb, Dm','Am':'C, Dm, Em',
        'Em':'G, Am, Hm','Hm':'D, Em, Fm#','Fm#':'Cm#, A, Hm',
        'Cm#':'E, Gm#, Fm#','Gm#':'H, Emb, Cm#','Emb':'Gb (F#), Bmb, Gm#',
        'Bmb':'Gb (F#), Bmb, Gm#','Dm#':'Gb (F#), Bmb, Gm#','A#m':'Gb (F#), Bmb, Gm#',
        'Fm':'Cm, Ab, Bmb','Cm':'Eb, Gm, Fm','Gm':'Dm, Cm, Bb',
        'Dm':'Gm, Am, F',
    }
    if message.text == "че угодно" or message.text == "что угодно":
        answer = "А ты хорош."
    elif message.text in notes.keys():
        bot.send_message(message.chat.id, melody)
        for key, value in notes.items():
            if key == message.text:
                answer = 'Дальше можно: ' + value
    elif "убью" in message.text:
        answer = "Баюс баюс."
    # for particular person with that ID:
    elif message.text == "тост" and str(message.from_user.id) == str(mensiratus):
        answer = "Володя молодец!"
    elif 'в жопу раз' in message.text:
        answer = 'А сам-то одноглазый наверно?'
    elif 'два фуфела' in message.text:
        answer = 'Фуфел тут только ты.'
    elif message.text == "нет":
        answer = 'Пидора ответ.'
    elif 'братишка' in message.text:
        answer = 'Какой нахуй братишка? Ты меня уже доебал!'
    elif message.text in ['никак', "норм", "нормас", "плохо", "збс"]:
        answer = 'збс, я рад.'
    elif 'окбот' in message.text:
        quantity = random.randint(0, 100)
        black_list = ['сколько', 'какого', 'Сколько', 'Какого', 'куда', 'Куда', 'откуда', 'Откуда', "Когда", 'когда']
        answer = None
        for question in black_list:
            if question in message.text:
                answer = 'Не знаю. Такое можешь больше не спрашивать.'
        if answer is None:
            if quantity == 100:
                answer = 'Да, так и будет. Инфа соточка.'
            elif quantity > 90 and quantity != 100:
                answer = 'Считай что так и будет.'
            elif quantity > 80 and quantity < 90:
                answer = 'Я гарантирую это.'
            elif quantity > 70 and quantity < 80:
                answer = 'Скорее всего так и будет.'
            elif quantity > 60 and quantity < 70:
                answer = 'Я бы особо на это не надеялся.'
            elif quantity > 50 and quantity < 60:
                answer = '50 на 50'
            elif quantity > 40 and quantity < 50:
                answer = 'Шансы есть, а там кто знает.'
            elif quantity > 30 and quantity < 40:
                answer = 'Шансов мало, но они есть.'
            elif quantity > 20 and quantity < 30:
                answer = 'Ну хуй знает, наверно нет.'
            elif quantity > 10 and quantity < 20:
                answer = 'Вероятность этого КРАЙНЕ мала.'
            else:
                answer = 'Ха-ха! Даже не надейся.'
    else:
        answer = "Не понимаю, что ты пишешь. Лучше попробуй команды какие-нибудь. Или спроси любой вопрос. Напиши 'окбот' и твой вопрос."
    time.sleep(2)
    bot.send_message(message.chat.id, answer)



# Получение сообщений
@server.route("/bot", methods=['POST'])
def getMessage():
    # Чтение данных от серверов telegram
    bot.process_new_messages(
        [telebot.types.Update.de_json(request.stream.read().decode("utf-8")).message
        ])
    return "!", 200

# Установка webhook
@server.route("/")
def webhook():
    bot.remove_webhook()
    # Если вы будете использовать хостинг или сервис без https
    # то вам необходимо создать сертификат и
    # добавить параметр certificate=open('ваш сертификат.pem')
    return "%s" %bot.set_webhook(url=WEBHOOK_URL_BASE), 200

@server.route("/remove")
def remove_hook():
    bot.remove_webhook()
    return "Webhook has been removed"

# Запуск сервера
server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
webhook()


#if __name__ == '__main__':
#    bot.polling(none_stop=True, interval=0)