import random
import os

winner_dict = {('R','R'):0, ('R','P'):-1, ('R','S'):1 ,
               ('P','P'):0, ('P','S'):-1, ('P','R'):1 , 
               ('S','S'):0, ('S','R'):-1, ('S','P'):1 }
               
options = ('R', 'S', 'P')

showing = {'R' : 'Rock', 'S':'Scissors', 'P':'Papers'}

def game():

    computer_choice = random.choice(options)
    player_choice = str.upper(input('(R)ock , (P)aper or (S)cissors?' ))
    
    while player_choice not in options:
        print('\nYour answer is not correct....\n')
        player_choice = str.upper(input('(R)ock , (P)aper or (S)cissors?' ))
    
    choice_result = (player_choice, computer_choice)
    
    results = { 0 : 'Tie' , 1:'You Won' , -1:'You Lost'}
    print(f'\nYour chois:{showing[player_choice]}')
    print(f'computer chois:{showing[computer_choice]}')
    print(results[winner_dict[choice_result]])
    
game()
while True:
    retry = input('\nDo You Want to retry? y\n')
    if retry == 'y':
        os.system('clear')
        game()
    else:
        break