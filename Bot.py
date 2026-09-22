import os
import telebot
from telebot import types

TOKEN = os.getenv("8931464391:AAEJeZ7SLAbDU4BP6rtjGouvFUKZ-vFlo5w")

bot = telebot.TeleBot(8931464391:AAEJeZ7SLAbDU4BP6rtjGouvFUKZ-vFlo5w)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "🕵️ Ayg‘oqchi o‘yiniga xush kelibsiz!\n\n"
        "Bot ishlayapti ✅"
    )

@bot.message_handler(commands=["help"])
def help_command(message):
    bot.reply_to(
        message,
        "🎮 Ayg‘oqchi — Telegram guruhlarida o‘ynaladigan o‘yin.\n"
        "Keyingi bosqichda o‘yin funksiyalarini qo‘shamiz."
    )

print("Bot ishga tushdi...")
bot.infinity_polling()
