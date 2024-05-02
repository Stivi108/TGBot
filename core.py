from telebot import TeleBot
from telebot.types import Message
# from settings import bot
# from token import botKey
import webbrowser
from botKey import botKey


bot = TeleBot(botKey)


@bot.message_handler(commands=["web"])
def site(msg: Message):
    webbrowser.open('vk.com')

@bot.message_handler(commands=["start"])
def main(msg: Message):
    bot.send_message(chat_id=msg.chat.id, text="Привет! Рад знакомству!")


@bot.message_handler(commands=["hello", "hi"])
def hello_handler(msg: Message):
    bot.send_message(chat_id=msg.chat.id, text=f"Привет, {msg.from_user.first_name}! Рад знакомству!")


@bot.message_handler(content_types=["text", "photo"])
def echo_message_handler(msg: Message):
    if msg.text:  # equivalent to if msg.content_type == "text"
        bot.send_message(chat_id=msg.chat.id, text=msg.text)
    elif msg.photo:  # # equivalent to if msg.content_type == "photo"
        bot.send_message(chat_id=msg.chat.id, text="Крутое фото!")


@bot.message_handler()
def funs(msg: Message):
    if msg.text.lower() == 'запомни':
        bot.send_message(chat_id=msg.chat.id, text="Запомнил!")
    elif msg.text.lower() == 'id':
        bot.reply_to(msg, f'ID {msg.from_user.id}')

bot.infinity_polling()
