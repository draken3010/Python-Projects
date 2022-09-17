"""Welcome to Rock Paper Scissors"""

import random

print(f'Welcome to rock, paper, scissor \n Please enter your choice \n 1 for rock \n 2 for paper \n 3 for scissor')

user_inp = int(input("Enter your choice: "))

if user_inp == 1:
    user_choice = 'rock'
elif user_inp == 2:
    user_choice = 'paper'
else:
    user_choice = 'scissor'

# Printing user input
print(f'The user choice is {user_choice}')

print("Now computer's turn \n")

comp_choice_list = ['rock', 'paper', 'scissor']
comp_choice = random.choice(comp_choice_list)
# Printing the choice of computer
print(f'The computer choice is {comp_choice}')

def start_game():
    # Checking the condition of Draw (Both user and computer having same choice)
    if user_choice == comp_choice:
        print(f'Draw, as both user and computer have same choice')
    
    # Checking condition for win
    if user_choice == "rock" and comp_choice == "paper":
        print(f'Computer wins')
    elif user_choice == "rock" and comp_choice == "scissor":
        print(f'User wins')
    elif user_choice == "paper" and comp_choice == "scissor":
        print(f'Computer wins')
    elif user_choice == "paper" and comp_choice == "rock":
        print(f'User wins')
    elif user_choice == "scissor" and comp_choice == "rock":
        print("Computer wins")
    elif user_choice == "scissor" and comp_choice == "paper":
        print(f'User wins')

start_game()




