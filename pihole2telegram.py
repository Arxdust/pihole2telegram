import config
from telegram.ext import CommandHandler
from telegram.ext import Updater, CallbackQueryHandler
# from telegram.ext import MessageHandler, Filters
from telegram import ChatAction
from parse import genstats, top_it, check_status
import time
from kb import *

#import logging

#logging.basicConfig(level=logging.DEBUG,
#                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

bold = '*'
updater = Updater(token=config.token)
dispatcher = updater.dispatcher

def start(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id, text="Hi, I'm pihole bot")
    time.sleep(1)

    user = str(update.message.from_user.id)
    if user not in config.admin:
        bot.sendChatAction(chat_id=update.message.chat_id,
                           action=ChatAction.TYPING)

        time.sleep(1)
        userid = update.message.from_user.id
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="You are id not in admin list. :(\n You id is " + str(userid))
    else:
        bot.sendChatAction(chat_id=update.message.chat_id,
                           action=ChatAction.TYPING)
        bot.send_sticker(chat_id=update.message.chat_id, sticker='CAADAgADBQADqWzzCr24QnCkXz6YAg')
        time.sleep(2)
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="You can use me - /help.")


def help(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="/id - user id \n/pihole - Menu")


def myid(bot, update):
    userid = update.message.from_user.id
    bot.sendMessage(chat_id=update.message.chat_id, text=userid)


def pihole(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='Pi-hole 🌀', reply_markup=reply_markup)


def button(bot, update):
    query = update.callback_query

    if query.data == '1':
        bot.editMessageText(text=genstats(),
                            chat_id=query.message.chat_id,
                            message_id=query.message.message_id,
                            reply_markup=reply_markup,
                            parse_mode='Markdown')

    if query.data == '2':
        bot.editMessageText(text='Please choose:',
                            reply_markup=reply_markup2,
                            chat_id=query.message.chat_id,
                            message_id=query.message.message_id,
                            )

    if query.data == '4':
        bot.editMessageText(text=top_it('topClients'),
                            chat_id=query.message.chat_id,
                            message_id=query.message.message_id,
                            reply_markup=reply_markup2,
                            parse_mode='Markdown'

                            )

    if query.data == '5':
        bot.editMessageText(text=top_it('topItems', 1),
                            chat_id=query.message.chat_id,
                            message_id=query.message.message_id,
                            reply_markup=reply_markup2,
                            parse_mode='Markdown'
                            )

    if query.data == '6':
        bot.editMessageText(text=top_it('topItems', 2),
                            chat_id=query.message.chat_id,
                            message_id=query.message.message_id,
                            reply_markup=reply_markup2,
                            parse_mode='Markdown'
                            )

    if query.data == '3':
        bot.editMessageText(text='Please choose:',
                            reply_markup=reply_markup3,
                            chat_id=query.message.chat_id,
                            message_id=query.message.message_id
                            )

    if query.data == '7':
        bot.editMessageText(text=check_status('status'),
                            chat_id=query.message.chat_id,
                            message_id=query.message.message_id,
                            reply_markup=reply_markup3,
                            parse_mode='Markdown'
                            )

    if query.data == '8':
        bot.editMessageText(text=check_status('enable'),
                            chat_id=query.message.chat_id,
                            message_id=query.message.message_id,
                            reply_markup=reply_markup3,
                            parse_mode='Markdown'
                            )

    if query.data == '9':
        bot.editMessageText(text=check_status('disable'),
                            chat_id=query.message.chat_id,
                            message_id=query.message.message_id,
                            reply_markup=reply_markup3,
                            parse_mode='Markdown'
                            )

    if query.data == '10':
        bot.editMessageText(text = 'Pi-hole 🌀',
                            chat_id = query.message.chat_id,
                            message_id = query.message.message_id,
                            reply_markup = reply_markup,
                            parse_mode = 'Markdown')


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

myid_handler = CommandHandler('id', myid)
dispatcher.add_handler(myid_handler)

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

pihole_handler = CommandHandler('pihole', pihole)
dispatcher.add_handler(pihole_handler)

button_handler = CallbackQueryHandler(button)
dispatcher.add_handler(button_handler)

updater.start_polling()
