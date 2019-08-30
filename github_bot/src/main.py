import issue_func
import telebot
from telebot import apihelper
apihelper.proxy = {'https':'socks5h://Naatkok:jGgTzR7kvzIFpdReXcrd22V15MfHtDOKdSUbWXgH@vpnzone.technology:10580'}
try:
    import keys
except ImportError as e:
    print("Перед запуском бота необходимо создать файл с названием keys.py, где указать ключ от вашего робота и ключ от API  Подробнее читайте в файле readme.txt")
    raise e

bot = telebot.TeleBot(keys.bot);

@bot.message_handler(commands=['Проблема: '])
@bot.message_handler(content_types=['text'])

def send_text(message):
