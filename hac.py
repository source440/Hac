import telebot

# استبدل 'YOUR_BOT_TOKEN' بتوكن البوت الخاص بك
TOKEN = '8374000550:AAGRzSNoQx89m-KeOD83RzyPGBzQ0WV1Wts'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def reply_to_all(message):
    # الرد على أي رسالة بـ "اهلا بلاك"
    bot.reply_to(message, "اهلا بلاك")

# تشغيل البوت
print("Bot is running...")
bot.infinity_polling()
