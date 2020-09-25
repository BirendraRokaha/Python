# 2 player tic tac toe game with scorebord.

# Create a board/gamearea for the gameplay.
def board(values):
    # The game board
    print('\n')
    print('\t_________________')
    print('\t     |     |')
    print(f'\t  {values[0]}  |  {values[1]}  |  {values[2]}  ')
    print('\t_____|_____|_____')

    print('\t     |     |')
    print(f'\t  {values[3]}  |  {values[4]}  |  {values[5]}  ')
    print('\t_____|_____|_____')

    print('\t     |     |')
    print(f'\t  {values[6]}  |  {values[7]}  |  {values[8]}  ')
    print('\t_____|_____|_____')
    print('\n')

def game(cur_player):

    # values for the position in the board.
    values = [' ' for x in range(9)]

    # player position store
    player_pos = {'X':[],'Y':[]}

    # Main game Loop
    while True:
        board(values)

def scorebord():
    pass

if __name__ == '__main__':
    print('-------- Tic Tac Toe --------')

    # Players
    player1 = 'Player1'
    player2 = 'Player2'






