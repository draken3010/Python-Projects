'''Welcome to rolling dice stimualtor - Lost your dice? Dont worry, just run this program and your problem will be solved'''

import random

def roll_dice():
    choice_list = [1,2,3,4,5,6]
    return random.choice(choice_list)

print(roll_dice())