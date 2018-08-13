from telegram import InlineKeyboardButton, InlineKeyboardMarkup


keyboard = [[InlineKeyboardButton("📊 General Stats 📊", callback_data='1')],
            [InlineKeyboardButton("📋 Top Items 📋", callback_data='2')],
            [InlineKeyboardButton("⚙ Management ⚙", callback_data='3')]]

keyboard2 = [[InlineKeyboardButton("Top Clients", callback_data='4')],
             [InlineKeyboardButton("Top Queries", callback_data='5'),
              InlineKeyboardButton("Top Ads", callback_data='6')],
             [InlineKeyboardButton("Main Menu", callback_data='10')]]

keyboard3 = [[InlineKeyboardButton("Status", callback_data='7')],
             [InlineKeyboardButton("Enable✅", callback_data='8'), InlineKeyboardButton("Disable❌", callback_data='9')],
             [InlineKeyboardButton("Main Menu", callback_data='10')]]








reply_markup = InlineKeyboardMarkup(keyboard)
reply_markup2 = InlineKeyboardMarkup(keyboard2)
reply_markup3 = InlineKeyboardMarkup(keyboard3)