import random
import telebot
from BotStats import bot

symbols = ["🍒", "🍋", "🍊", "🍇", "🍉", "🍎"]

   
     
def lose_variant():
    first_symbol = random.choice(symbols) 
    second_symbol = random.choice(symbols) 
    third_symbol = random.choice(symbols)
    multiplier = 0
    if first_symbol == second_symbol[0] and first_symbol == third_symbol[0]:
       lose_variant()
    else:
       return [first_symbol , second_symbol , third_symbol , multiplier]
    
def fifteen_percent_variant():
    first_symbol = "🍎"
    second_symbol = "🍎"
    third_symbol = "🍎"
    multiplier = 1.5
    return [first_symbol , second_symbol , third_symbol , multiplier]

def ten_percent_variant():
    first_symbol = "🍉"
    second_symbol = "🍉"
    third_symbol = "🍉"
    multiplier = 1.7
    return [first_symbol , second_symbol , third_symbol , multiplier]

def seven_percent_variant():
    first_symbol = "🍇"
    second_symbol = "🍇"
    third_symbol = "🍇"
    multiplier = 2
    return [first_symbol , second_symbol , third_symbol , multiplier]

def six_percent_variant():
    first_symbol = "🍊"
    second_symbol = "🍊"
    third_symbol = "🍊"
    multiplier = 2.5
    return [first_symbol , second_symbol , third_symbol , multiplier]

def six_percent_variant():
    first_symbol = "🍋"
    second_symbol = "🍋"
    third_symbol = "🍋"
    multiplier = 5
    return [first_symbol , second_symbol , third_symbol , multiplier]

def three_percent_variant():
    first_symbol = "🍒"
    second_symbol = "🍒"
    third_symbol = "🍒"
    multiplier = 7
    return [first_symbol , second_symbol , third_symbol , multiplier]



def game_decision():
    percent = random.randint(1, 100)
    
    if percent > 55 and percent <= 70:
        return fifteen_percent_variant()
    elif percent > 70 and percent <= 80:
        return ten_percent_variant()
    elif percent > 80 and percent <= 87:
        return seven_percent_variant()
    elif percent > 87 and percent <= 93:
        return six_percent_variant()
    elif percent > 93 and percent <= 97:
        return six_percent_variant()
    elif percent > 97 and percent <= 100:
        return three_percent_variant()
    elif percent <= 55 :
        return lose_variant()
    
