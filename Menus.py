import telebot
from telebot import types
import random
from SlotGame import slot_game
from BotStats import bot
from InformationMessage import informationMessage


@bot.message_handler(commands=['start'])
def start(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        play = types.KeyboardButton('Play🎰')
        balance = types.KeyboardButton('Balance💵')
        information = types.KeyboardButton('Informationℹ️')
        support = types.KeyboardButton('Support🔴')
        markup.add(play , balance , information , support)

        bot.send_message(message.chat.id , f'Hello {message.from_user.first_name} , this is casino mini game bot! ' , reply_markup=markup) 




def back_markup(message):
 markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

 play = types.KeyboardButton('Play🎰')
 balance = types.KeyboardButton('Balance💵')
 information = types.KeyboardButton('Informationℹ️')
 support = types.KeyboardButton('Support🔴')
 markup.add(play , balance , information , support)

 bot.send_message(message.chat.id , 'Back⬅️' , reply_markup=markup)


def play_variant(message):
 if message.text == 'Play slot🎰':
                 slot_game(message)
 elif message.text == 'Make a bet💵':
                 bot.send_message(message.chat.id , 'Comming soon!')    
 elif message.text == 'Back⬅️':
                 back_markup(message)

def play_markup(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    play_slot = types.KeyboardButton('Play slot🎰')
    make_bet = types.KeyboardButton('Make a bet💵')
    back = types.KeyboardButton('Back⬅️')

    markup.add(play_slot , make_bet , back)

    bot.send_message(message.chat.id , 'Play🎰' , reply_markup=markup)

def balance_markup(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    deposit = types.KeyboardButton('Deposit💳')
    withdraw = types.KeyboardButton('Withdraw🔻')
    my_balance = types.KeyboardButton('My balance🪙')
    back = types.KeyboardButton('Back⬅️')

    markup.add(deposit, withdraw , my_balance , back)

    bot.send_message(message.chat.id , 'Balance💵' , reply_markup=markup)

def balance_variant(message):
    if message.text == 'Deposit💳':
        bot.send_message(message.chat.id , 'Comming soon!')
    elif message.text == 'Withdraw🔻':
        bot.send_message(message.chat.id , 'Comming soon!')
    elif message.text == 'My balance🪙':
        bot.send_message(message.chat.id , 'Comming soon!')
    elif message.text == 'Back⬅️':
        back_markup(message)

def information_markup(message):
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

      back = types.KeyboardButton('Back⬅️')

      markup.add(back)
      bot.send_message(message.chat.id , informationMessage , reply_markup=markup)

def information_variant(message):
    if message.text == 'Back⬅️':
        back_markup(message)

def support_markup(message):
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

      back = types.KeyboardButton('Back⬅️')

      markup.add(back)
      bot.send_message(message.chat.id , 'Support🔴' , reply_markup=markup)

def support_variant(message):
      if message.text == 'Support🔴':
            bot.send_message(message.chat.id , 'Write down your problem please:' )
      elif message.text == 'Back⬅️':
            back_markup(message)


@bot.message_handler(content_types=['text'])
def menu(message):
    if message.chat.type != 'private':
        return

    if message.text == 'Play🎰':
        play_markup(message)
    elif message.text in ['Play slot🎰', 'Make a bet💵', 'Back⬅️']:
        play_variant(message)
    elif message.text == 'Balance💵':
        balance_markup(message)
    elif message.text in ['Deposit💳', 'Withdraw🔻', 'My balance🪙', 'Back⬅️']:
        balance_variant(message)
    elif message.text == 'Informationℹ️':
        information_markup(message)
    elif message.text == 'Informationℹ️':
        information_variant(message)
    elif message.text =='Support🔴':
        support_markup(message)
    elif message.text == 'Support🔴':
        support_variant(message)