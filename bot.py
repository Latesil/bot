#бот
import telebot
import os
import constants
import random
import urllib.request as urllib2
import requests
import time
from bs4 import BeautifulSoup

mensiratus = 171568889
i_am = 170060564
soider = 75266684
stolen = 167379044


bot = telebot.TeleBot(constants.token)

#send message to smth
#bot.send_message(stolen, "Бля, охуенная пикча.")

#update
# upd = bot.get_updates()
#returns in dict format

#last update from all upds
# last_upd = upd[-1]

#all messages from last upd
# message_from_user = last_upd.message

print(bot.get_me())
#log message and answer
def log(message, answer):
    from datetime import datetime
    #time now for message
    print("\n ------")
    print(datetime.now())
    print("Message from {0} {1}. (id = {2}) \n Text: - {3}".format(message.from_user.first_name,
    message.from_user.last_name, str(message.from_user.id), message.text))
    print(answer)

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
    user_markup.row('/foto', '/help', '/2ch')
    bot.send_message(message.from_user.id, "Привет, человек. Напиши мне че угодно.", reply_markup=user_markup)

#stop keyboard
@bot.message_handler(commands=['stop'])
def handle_start(message):
    hide_markup = telebot.types.ReplyKeyboardHide
    bot.send_message(message.from_user.id, "..", reply_markup=hide_markup)
#send foto 
#@bot.message_handler(commands=['foto'])
#def send_photo(message):
#    bot.send_chat_action(message.from_user.id, 'upload_photo')
#    directory = "d:/PYTHON/Telega/Fotos/"
#    all_files_in_directory = os.listdir(directory)
#    random_file = random.choice(all_files_in_directory)
#    img = open(directory + random_file, 'rb')
#    bot.send_photo(message.from_user.id, img, reply_to_message_id=message.message_id)
#    img.close()
#    answer = "Отправил" + ' ' + random_file
#    log(message, answer)

#foto from internet
@bot.message_handler(commands=['2ch'])
def from_url(message):
    all_boards = [
        'b', 'au','bi','biz','bo','c','em','fa','fiz',
        'fl','ftb','hh','hi','me','mg','mlp','mo', 'b',
        'mov','mu','ne','psy','re','sci','sf','sn', 'b',
        'sp','spc','tv','un','w','wh','wm','wp','zog', 'b',
        'de','di','diy','mus','pa','p','wrk','trv', 'b',
        'gd','hw','mobi','pr','ra','s','t','web','bg', 'b',
        'cg','ruvn','tes','v','vg','wr','a','fd','ja', 'b',
        'ma','vn','b','o','soc','media','r', 'aa', 'abu',
        'rf','fg','fur','ga','vape','h','ho','hc', 'b',
        'e','fet','sex','fag','int','po','news','dev','gg'
    ]
    board = all_boards[random.randint(1, (len(all_boards)))] #letter
    list_urls = []
    time.sleep(0.5)
    bot.send_message(message.chat.id, "Щас, секунду...")
    len_board = len(board)
    board_url = 'https://2ch.hk/' + board + '/'
    source_code = requests.get(board_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'lxml')
    for img in soup.findAll('a', {'name': 'expandfunc'}):
        link_to_image = img.get('href')
        #print(link_to_image)
        #add links on threads to list
        if link_to_image is not None and '.webm' not in link_to_image and '.gif' not in link_to_image:
                list_urls.append(board_url[:-1] + link_to_image[len_board+1:])
    url = list_urls[random.randint(0, (len(list_urls)-1))]
    time.sleep(2)
    bot.send_photo(message.from_user.id, url, reply_to_message_id=message.message_id)
    time.sleep(2)
    if board == 'ga':
        bot.send_message(message.chat.id, "Петушок, эта картинка была специально для тебя, прямиком из:" + " " + board_url)
    else:
        bot.send_message(message.chat.id, "Ну как? Кстати, я эту картинку взял отсюда:" + " " + board_url)
    answer = "Отправил" + ' ' + url
    log(message, answer)
#responses for message (or from_user.id)
@bot.message_handler(content_types=['text'])
def handle_text(message):
    melody = """Там.. татарам-тара-там...
        татара-тара-там..
        тра-та-тара-тара-там
        ТА-ТА..."""
    notes = {
        'C':'Дальше можно: G, Am, F','G':'Дальше можно: C, Em, D','D':'Дальше можно: G, Hm, A',
        'A':'Дальше можно: E, Fm#, D','E':'Дальше можно: A, Cm#, H','H':'Дальше можно: Gm#, Gb (F#), E',
        'Gb':'Дальше можно: Db, Emb, H','F#':'Дальше можно: Db, Emb, H','Db':'Дальше можно: Bm b, Gb (F#), Ab',
        'C#':'Дальше можно: Bm b, Gb (F#), Ab','G#':'Дальше можно: Eb, Fm, Db','Ab':'Дальше можно: Eb, Fm, Db',
        'Eb':'Дальше можно: Bb, Cm, Ab','D#':'Дальше можно: Bb, Cm, Ab','Bb':'Дальше можно: Gm, Eb, F',
        'A#':'Дальше можно: Gm, Eb, F','F':'Дальше можно: C, Bb, Dm','Am':'Дальше можно: C, Dm, Em',
        'Em':'Дальше можно: G, Am, Hm','Hm':'Дальше можно: D, Em, Fm#','Fm#':'Дальше можно: Cm#, A, Hm',
        'Cm#':'Дальше можно: E, Gm#, Fm#','Gm#':'Дальше можно: H, Emb, Cm#','Emb':'Дальше можно: Gb (F#), Bmb, Gm#',
        'Bmb':'Дальше можно: Gb (F#), Bmb, Gm#','Dm#':'Дальше можно: Gb (F#), Bmb, Gm#','A#m':'Дальше можно: Gb (F#), Bmb, Gm#',
        'Fm':'Дальше можно: Cm, Ab, Bmb','Cm':'Дальше можно: Eb, Gm, Fm','Gm':'Дальше можно: Dm, Cm, Bb',
        'Dm':'Дальше можно: Gm, Am, F',
    }
    if message.text == "че угодно" or message.text == "что угодно":
        answer = "А ты хорош."
    elif message.text in notes.items():
        bot.send_message(message.chat.id, melody)
        for key, value in notes.items():
            if key == message.text:
                answer = value
    elif "убью" in message.text:
        answer = "Баюс баюс."
    # for particular person with that ID:
    elif message.text == "тост" and str(message.from_user.id) == str(mensiratus):
        answer = "Володя молодец!"
    elif 'в жопу раз' in message.text:
        answer = 'А сам-то одноглазый наверно?'
    elif 'два фуфела' in message.text:
        answer = 'Фуфел тут только ты.'
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
            elif quantity > 70 and quantity < 90:
                answer = 'Скорее всего так и будет.'
            elif quantity > 50 and quantity < 70:
                answer = 'Шансы неплохи.'
            elif quantity > 30 and quantity < 50:
                answer = 'Ну хуй знает, наверно нет.'
            elif quantity > 10 and quantity < 30:
                answer = 'Вероятность этого КРАЙНЕ мала.'
            else:
                answer = 'Ха-ха! Даже не надейся.'
    else:
        answer = "Не понимаю, что ты пишешь. Лучше попробуй команды какие-нибудь. Или спроси любой вопрос. Напиши 'окбот' и твой вопрос."
    time.sleep(2)
    bot.send_message(message.chat.id, answer)
    log(message, answer)



bot.polling(none_stop=True, interval=0)