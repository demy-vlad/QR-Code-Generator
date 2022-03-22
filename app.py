import qrcode
from loguru import logger
from telebot import types
import telebot

bot = telebot.TeleBot("")
# bot.remove_webhook()

@bot.message_handler(commands=['start'])
def start(message):
        logger.debug(f"{message.chat.id, message.chat.username, message.chat.last_name, message.chat.first_name} - click: start")
        
        keyboard = types.InlineKeyboardMarkup()
        urls = types.InlineKeyboardButton("Generate URL QR-code", callback_data='url')
        keyboard.add(urls)
        bot.send_message(message.chat.id, "♦️ Create your own QR code in seconds ♣️", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call:True)
def founded_menu_faq(call):
        if call.data == "url":
                print(2)
                global qr_size
                global qr_version
                keyboard = types.InlineKeyboardMarkup()
                size_1 = types.InlineKeyboardButton("63✖️63", callback_data='size_1')                 
                size_3 = types.InlineKeyboardButton("117✖️117", callback_data='size_3')
                size_5 = types.InlineKeyboardButton("195✖️195", callback_data='size_5')
                size_7 = types.InlineKeyboardButton("273✖️273", callback_data='size_7')
                size_9 = types.InlineKeyboardButton("351✖️351", callback_data='size_9')
                size_15 = types.InlineKeyboardButton("945✖️945", callback_data='size_15')

                keyboard.add(size_1, size_3, size_5)
                keyboard.add(size_7, size_9, size_15)
                bot.send_message(call.message.chat.id, "Select QR code size:", reply_markup=keyboard)
                # bot.register_next_step_handler(msg)
        elif call.data == "size_1":
                qr_version = 3
                qr_size = 1
                msg = bot.send_message(call.message.chat.id, text=f"Enter URL:", parse_mode= "Markdown")
                bot.register_next_step_handler(msg, qacode)

        elif call.data == "size_3":
                qr_version = 5
                qr_size = 3
                msg = bot.send_message(call.message.chat.id, text=f"Enter URL:", parse_mode= "Markdown")
                bot.register_next_step_handler(msg, qacode)

        elif call.data == "size_5":
                qr_version = 5
                qr_size = 5
                msg = bot.send_message(call.message.chat.id, text=f"Enter URL:", parse_mode= "Markdown")
                bot.register_next_step_handler(msg, qacode)

        elif call.data == "size_7":
                qr_version = 5
                qr_size = 7
                msg = bot.send_message(call.message.chat.id, text=f"Enter URL:", parse_mode= "Markdown")
                bot.register_next_step_handler(msg, qacode)

        elif call.data == "size_9":
                qr_version = 10
                qr_size = 9
                msg = bot.send_message(call.message.chat.id, text=f"Enter URL:", parse_mode= "Markdown")
                bot.register_next_step_handler(msg, qacode)

        elif call.data == "size_15":
                qr_version = 10
                qr_size = 15
                msg = bot.send_message(call.message.chat.id, text=f"Enter URL:", parse_mode= "Markdown")
                bot.register_next_step_handler(msg, qacode)



def qacode(message):
        input_url = message.text
        qr = qrcode.QRCode(
                version=qr_version,
                box_size=qr_size,
                border=3)
        qr.add_data(input_url)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save(f'img/{message.chat.id}.png')

        file = open(f'img/{message.chat.id}.png', 'rb')
        bot.send_photo(message.chat.id, file)
        start(message)

bot.polling(none_stop=True)