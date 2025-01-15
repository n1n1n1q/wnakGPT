import telebot
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda msg: True)
def test_msg(message):
    bot.reply_to(message, message.text.lower())

def start_bot() -> None:
    print(BOT_TOKEN)
    bot.infinity_polling()
