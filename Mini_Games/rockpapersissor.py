import random

def rockpaper():

    points_comp = 0
    points_user = 0
    game_items = ['rock','paper','sissors']
    time = 0
    outcomes = {
        'rock':{'rock': 'draw', 'paper': 'lost', 'sissors':'won'},
        'paper':{'rock': 'won', 'paper': 'draw', 'sissors':'lost'},
        'sissors':{'rock': 'lost', 'paper': 'won', 'sissors':'draw'}
                }

    while time <3:
        user_input = ''
        while user_input not in game_items:
            user_input = input('Rock Paper Sissors : ').lower()
        time += 1
        comp_input = random.choice(game_items)


        print(f'Your choise : {user_input}')
        print(f'Computer choise  :{comp_input}')
        print(f'{outcomes[user_input][comp_input]}')

        if outcomes[user_input][comp_input] == 'won':
            points_user +=1
        elif outcomes[user_input][comp_input] == 'lost':
            points_comp +=1

    print(f'User Points : {points_user}')
    print(f'Comp Points : {points_comp}')
    if points_user > points_comp:
        print('You Won')
    elif points_user == points_comp:
        print('Draw')
    else:
        print('You Lost')

    play_again = input('Play again Y/N').lower()
    if play_again == 'y':
        rockpaper()
    else:
        print('thanks!!')


rockpaper()

