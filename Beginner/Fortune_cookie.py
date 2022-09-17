'''Fortune Cookie - Lets check whats your fortune today'''

# Using random module
import random

def future():
    fortune_list = ['A beautiful, smart, and loving person will be coming into your life.',
                    'A dubious friend may be an enemy in camouflage.',
                    'A faithful friend is a strong defense.',
                    'A feather in the hand is better than a bird in the air.',
                    'A fresh start will put you on your way.']
    
    # random module contains choice() that returns a random value from list,set,tuple etc
    return random.choice(fortune_list)

print(future())
    