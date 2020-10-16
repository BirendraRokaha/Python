'''
Testing for the likePokemon battle game
'''


# Pokemon class defines a pokemon object
class Pokemon():
    # Attributes
    def __init__(self,name,level,ptype):
        self.name = name
        self.level = level
        self.ptype = ptype
        self.healthp = 100 + (self.level * 5)
        self.attacks_list = ['tackle','growl']


    # Methods

    def get_stats(self):
        attackp = 25 + (self.level * 2)
        defensep = 25 + (self.level * 2)
        return attackp,defensep



# Basic Pokemon List just for testing initially
Pikachu = Pokemon(name='Pikachu',level=5,ptype='ELE')
Charmainder = Pokemon(name='Charmainder',level=5,ptype='FIR')
Bulbasaur =  Pokemon(name='Bulbasaur',level=5,ptype='GRA')
Squirtle = Pokemon(name='Squirtle',level=5,ptype='WAT')
Abra = Pokemon(name='Abra',level=10,ptype='PSY')

List_of_Pokemon = [Pikachu,Charmainder,Bulbasaur,Squirtle,Abra]

for pok in List_of_Pokemon:
    print(f'{pok.name} {pok.level} {pok.ptype} {pok.healthp} {pok.attacks_list}')


print(Pikachu.get_stats())
