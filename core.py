
from telebot.types import Message
from settings import bot




@bot.message_handler(commands=["hello", "hi"])
def hello_handler(msg: Message):
    bot.send_message(chat_id=msg.chat.id, text="Привет! Рад знакомству!")


@bot.message_handler(content_types=["text", "photo"])
def echo_message_handler(msg: Message):
    if msg.text:  # equivalent to if msg.content_type == "text"
        bot.send_message(chat_id=msg.chat.id, text=msg.text)
    elif msg.photo:  # # equivalent to if msg.content_type == "photo"
        bot.send_message(chat_id=msg.chat.id, text="Крутое фото!")


bot.infinity_polling()
