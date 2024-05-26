import telebot
from telebot import types
import random
from BotStats import bot
import time
from SymbolsChances import game_decision

symbols = ["🍒", "🍋", "🍊", "🍇", "🍉", "🍎"]
dot = '🍐'
message_on_casino_start = "Casino , casino , casino!"



def slot_game(message):
    msg = bot.send_message(message.chat.id, message_on_casino_start)

    variant_symbol = game_decision()

    first_symbol = variant_symbol[0]
    second_symbol = variant_symbol[1] 
    third_symbol = variant_symbol[2]
    multiplier = variant_symbol[3]

    firs_slot(message , msg , first_symbol)
    second_slot(message , msg , first_symbol , second_symbol)
    third_slot(message , msg , first_symbol , second_symbol , third_symbol) 


    if first_symbol == second_symbol[0] and first_symbol == third_symbol[0]:
        bot.send_message(message.chat.id , f'You win! {multiplier}x')
    else:
        bot.send_message(message.chat.id , 'You lose!')





def firs_slot(message , msg , first_symbol):
    for i in range(0 , 5):
        random_symbol = symbols[i]
        bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text=f" {random_symbol}")
        time.sleep(0.2)
    
    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text=f" {dot}")
     
    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text=f" {first_symbol}")

    time.sleep(0.2)

def second_slot(message , msg , first_symbol , second_symbol):
    
    for i in range(0 , 5):
        random_symbol = symbols[i]
        bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text=f" {first_symbol}  {random_symbol}")
        time.sleep(0.2)

    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text=f" {first_symbol} {dot}")

    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text=f" {first_symbol} {second_symbol[0]}")

    time.sleep(0.2)

def third_slot(message , msg , first_symbol , second_symbol , third_symbol):
    for i in range(0 , 5):
        random_symbol = symbols[i]
        bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text=f" {first_symbol}  {second_symbol[0]}  {random_symbol}")
        time.sleep(0.2)  

    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text=f" {first_symbol} {second_symbol} {dot}")
    
    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text=f" {first_symbol} {second_symbol[0]} {third_symbol[0]}")

    time.sleep(0.2)

        