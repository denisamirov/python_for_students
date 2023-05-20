import telebot
from telebot import types

token = 'YOUR_API_KEY'

bot=telebot.TeleBot(token)
    
@bot.message_handler(commands=['start'])
def start_message(message):
  markup = types.InlineKeyboardMarkup()
  buttonLink = types.InlineKeyboardButton("Сайт робототехники", 
                                          url='https://roboclub.space', 
                                          reply_markup=markup)
  markup.add(buttonLink)

  bot.send_message(message.chat.id, "Привет, {0.first_name}!"
                   "Нажми на кнопку и перейди на сайт)".format(message.from_user), 
                   reply_markup=markup)
  
@bot.message_handler(content_types='text')
def start_message(message):
  if message.text.lower() == 'привет':
    bot.send_message(message.chat.id, 
                     f'Привет, {message.chat.username}')
    
  else:
        bot.send_message(message.chat.id, 
                    f'Я не понял тебя, {message.chat.username}!')


bot.polling()
