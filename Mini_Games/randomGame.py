# simple game guessing game made in python

from random import *

# shuffel the game list list
def randomiser(game_list):
    shuffle(game_list)
    return game_list

# input the player guess
def guess():
    guess = 0
    while guess not in [1,2,3]:
            guess = int(input("Pick a number form 1 ,2 or 3: "))
    return guess


# The Game Logic checks if the player input is equal to the list
def game(game_list,player_guess):

    if game_list[player_guess-1] == 'O':
        print("You Did It!!!")
        print(player_guess)
        print(game_list)
    else:
        print("Better luck next time")
        print(player_guess)
        print(game_list)

# the game list
game_list = ['','O','']

# randomise the list
randomiser(game_list)

# input the player guess
player_guess = guess()

# run the game Logic
game(game_list,player_guess)

