import random

user_wins = 0
computer_wins = 0

while True:
    user_input = ("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == 'q':
        break
    
    if user_input not in ['rock', "paper", 'scissors']:
        continue

    