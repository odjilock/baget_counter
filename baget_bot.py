import telebot
from telebot import types
from email.message import Message

from sqlite import show_all_items


bot = telebot.TeleBot('5715647780:AAFosHKVw3LGv_ifudkpGua6xCXDr-YDyuI')


@bot.message_handler(commands=['start'])
def menu(message):
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     button_list = types.KeyboardButton('📋список багетов')
     button_info = types.KeyboardButton('BagetInfo')
     markup.add(button_list, button_info)
     bot.send_message(message.chat.id, 'меню' ,reply_markup=markup)


@bot.edited_channel_post_handler(content_types=['text'])
@bot.message_handler(content_types=['text'])
def show_menu(message: Message):
    text = message.text
    if text == '📋список багетов':
        bot.send_photo(message.chat.id, photo=open('images/baget_list.jpg', 'rb'))
    
    elif text == 'BagetInfo':
        all_bagets = show_all_items()
        for key, value in all_bagets:
            if value <= 2:
                bot.send_message(message.chat.id, f'{key}-{value} 🛑')
            else:
                bot.send_message(message.chat.id, f'{key}-{value}')    
            

                




bot.polling(non_stop=True)