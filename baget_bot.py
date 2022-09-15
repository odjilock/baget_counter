import telebot
from telebot import types
from email.message import Message
import sqlite3

from sqlite import count_minus_one, show_all_items, show_count_of_baget


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
       
        
    ###доделать elif '-' in text:
        try:
            str_list = []
            for i in text:
                str_list.append(i)
            print(str_list)
            string_number = ''.join(str_list)
          
            for i in range(len(string_number)):
                string_number.remove('-')
                
            
            print(string_number)
            count_minus_one(string_number)
            bot.send_message(message.chat.id, f'багет #{string_number} вычтен\
            осталось {show_count_of_baget(string_number)}" !')
        except sqlite3.OperationalError:
            bot.send_message(message.chat.id, f'проверьте правильность команды\n\
            {text}\n вычитание "-" должны быть указанно после номера багета')
   




# list = []
#             for element in text:
#                 list.append(element)


#             string_number = ''.join(list)
#             try:
#                 for i in range(len(str)):
#                     list.remove('-')
#             except ValueError:
#                 print('delete complete')





bot.polling(non_stop=True)