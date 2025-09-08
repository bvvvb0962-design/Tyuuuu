import telebot
import os

TOKEN = os.getenv("7699584421:AAEJwX-zwh1pK9v4jFGQlXOL8NKzsPS9xro")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "سلام! ربات آنلاین شد 🚀 (Koyeb)")

print("🤖 Bot started...")
bot.polling()
