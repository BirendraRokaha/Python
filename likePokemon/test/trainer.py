'''
Trainer object details
'''

from pokemom import *


class Traier():
    def __init__(self,name,is_player,pokemon_list):
        self.name = name
        self.is_player = is_player
        self.pokemon_list = pokemon_list

    def trainer_details(self):
        print(f'{self.name} is player {self.is_player}')
        print('Pokemon List')
        for pok in self.pokemon_list:
            print(f'Name = {pok.name} level {pok.level}')
        print('')

Ash = Traier(name='Ash',is_player=True,pokemon_list=[Pikachu,Charmainder])

Garry = Traier(name='Garry',is_player=False,pokemon_list=[Squirtle,Abra])


Ash.trainer_details()



Garry.trainer_details()
