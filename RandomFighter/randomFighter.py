'''
Random fighter is a 2 player fighter silulator.
'''

import time
import random as rd


def attack(power,name):
    # Randomly selects an attack
    attack_type = rd.randint(1,5)

    if attack_type == 1:
        power = 10
        name = 'Kick'

    if attack_type == 2:
        power = 5
        name = 'Punch'

    if attack_type == 3:
        power = 7
        name = 'Doubble Punch'

    if attack_type == 4:
        power = -2
        name = 'Gained HP and Leach'

    if attack_type == 5:
        power = 0
        name = 'Miss'

    return power,name


def fight(pname1,pname2):
    # Setting up player Health
    p1_health = 100
    p2_health = 100

    attack_power = 0
    attack_name = ''
    print('---------- LET THE BATTLE BEGIN ----------')

    # Main game loop
    while True:

        # Randomly assigns turn to players
        attack_turn = rd.randint(1,2)

        # Which attack and its power
        attack_power, attack_name = attack(attack_power,attack_name)


        # Player with turn attacks
        if attack_turn == 1:
            p2_health -= attack_power
            print(f'-------- {pname1} {attack_name}ed {pname2} ---------')
            print(f'-- Status : {pname1} {p1_health} HP | {pname2} {p2_health} HP --')

        if attack_turn == 2:
            p1_health -= attack_power
            print(f'-------- {pname2} {attack_name}ed {pname1} ---------')
            print(f'-- Status : {pname1} {p1_health} HP | {pname2} {p2_health} HP --')

        # Blank line and sleep timer
        print('')
        time.sleep(1.10)

        # Break loop if player health is 0
        if (p1_health <= 0) or (p2_health <= 0):
            break

    # Game Over messages
    print('---------- GAME OVER ----------')
    if p1_health <= 0:
        print(f'---- {pname2} WON ----')
        print(f'---- {pname1} is DEAD ----')

    if p2_health <= 0:
        print(f'---- {pname1} WON ----')
        print(f'---- {pname2} is DEAD ----')



if __name__ == '__main__':

    # Player 1 and player 2
    pname1 = 'Ron Ron'
    pname2 = 'Nor Nor'


    # Run the Game
    fight(pname1,pname2)

else:
    print('System Error')

