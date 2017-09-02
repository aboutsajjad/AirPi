from telegram.ext import Updater, CommandHandler
from airpi import AirPi
airpi = AirPi()

def now(bot, update):
    bot.send_message(update.message.chat_id, airpi.pretty_string())

def file(bot, update):
    bot.send_document(update.message.chat_id, open('data.csv', 'rb'))



def main():
    
    updater = Updater("374973762:AAGzYwbJKt-iwhcr5wjOUA8oF_wQTszh9qA")
    updater.dispatcher.add_handler(CommandHandler('now', now))
    updater.dispatcher.add_handler(CommandHandler('file', file))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
