import telebot
from telebot import types
from email.message import Message
import sqlite3
from sqlite import count_minus_one, count_plus_one, show_all_items, show_count_of_baget


bot = telebot.TeleBot('5715647780:AAFosHKVw3LGv_ifudkpGua6xCXDr-YDyuI')


@bot.message_handler(commands=['start', 'меню', 'menu', 'info'])
def menu_buttons(message):
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     button_list = types.KeyboardButton('📋список багетов')
     button_info = types.KeyboardButton('BagetInfo')
     markup.add(button_list, button_info)
     bot.send_message(message.chat.id, 'меню' ,reply_markup=markup)


@bot.edited_channel_post_handler(content_types=['text'])
@bot.message_handler(content_types=['text'])
def add_and_remove_products(message: Message):
    text = message.text
    if text == '📋список багетов':
        bot.send_photo(message.chat.id, photo=open('images/baget_list.jpg', 'rb'))
    elif text == 'BagetInfo':
        all_bagets = show_all_items()
        
        bot.send_message(
            message.chat.id,f'полный список багетов с количеством реек\n\
🛑 = осталось меньше двух реек!',
        reply_to_message_id=message.message_id)

        for key, value in all_bagets:
            if value <= 2:
                bot.send_message(message.chat.id, f'#{key} | {value} 🛑')
            else:
                bot.send_message(message.chat.id, f'#{key} | {value} ')    
       
        
    elif text == '1-' or text == '2-' or text == '3-' or text == '3-'\
        or text == '4-' or text == '5-' or text == '6-' or text == '7-'\
        or text == '8-' or text == '9-' or text == '10-' or text == '11-'\
        or text == '12-' or text == '13-' or text == '14-' or text == '15-'\
        or text == '16-' or text == '17-' or text == '18-' or text == '19-'\
        or text == '20-' or text == '21-' or text == '22-' or text == '23-'\
        or text == '24-' or text == '25-' or text == '26-' or text == '27-':

        temporary_list = []
        for i in text:
            temporary_list.append(i)

        temporary_list.remove('-')
        refresh_text = ''.join(temporary_list)
        
        count_minus_one(refresh_text)

        bot.send_photo(
                        message.chat.id, photo=open(\
                        f'images/{refresh_text}.jpg','rb'),\
                        reply_to_message_id=message.message_id
                                                                )
        bot.send_message(message.chat.id, f'багет #{refresh_text} - удалён\
        \nосталось = {show_count_of_baget(refresh_text)}')


    elif text == '1+' or text == '2+' or text == '3+' or text == '3+'\
        or text == '4+' or text == '5+' or text == '6+' or text == '7+'\
        or text == '8+' or text == '9+' or text == '10+' or text == '11+'\
        or text == '12+' or text == '13+' or text == '14+' or text == '15+'\
        or text == '16+' or text == '17+' or text == '18+' or text == '19+'\
        or text == '20+' or text == '21+' or text == '22+' or text == '23+'\
        or text == '24+' or text == '25+' or text == '26+' or text == '27+': 

        temporary_list = []
        for i in text:
            temporary_list.append(i)

        temporary_list.remove('+')
        refresh_text = ''.join(temporary_list)
        count_plus_one(refresh_text)

        bot.send_photo(
                        message.chat.id, photo=open(
                        f'images/{refresh_text}.jpg','rb'),
                        reply_to_message_id=message.message_id
                                                                )

        bot.send_message(message.chat.id, f'багет #{refresh_text} - добавлен\
        \nосталось = {show_count_of_baget(refresh_text)}')


    else:
        bot.send_message(message.chat.id, f'такой багет не распознан!\
        \n"{text}"')
        bot.send_message(message.chat.id,\
        f'КОМАНДЫ РАБОТЫ С БОТОМ:\
        \n\n\n1.Добавить багет\
        \nвведите номер багета вместе со знаком "+" как в примерe (23+)\
        \n\n\n2.Удалить багет\
        \nвведите номер багета вместе со знаком "-" как в примерe (11-)\\n\n\n\
                открыть меню - /menu\n\
        ')


bot.polling(non_stop=True)