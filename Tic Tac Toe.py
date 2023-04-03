def display_board(board):

    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])


def player_input():
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, Choose X or O: ').upper()

        player1 = marker

        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'

    return player1, player2

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board,mark):
    return ((board[1] == board[2] == board[3] == mark) or
           (board[4] == board[5] == board[6] == mark) or
           (board[7] == board[8] == board[9] == mark) or
           (board[7] == board[4] == board[1] == mark) or
           (board[8] == board[5] == board[2] == mark) or
           (board[9] == board[6] == board[3] == mark) or
           (board[7] == board[5] == board[3] == mark) or
           (board[9] == board[5] == board[1] == mark))

import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board,position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    # Board is full is it return True
    return True


def player_choice(board):
    position = 0

    while position not in range(1, 10) or not space_check(board, position):
        position = int(input('Choose a position (1-9): '))

    return position


def replay():
    choice = input('Play Again? Enter Yes or No: ')
    choice = choice.capitalize()
    return choice == 'Yes'


# While loop to keep running the game
print('Welcome to TIC TAC TOE')

while True:

    # Play the game
    # SET EVERYTHING UP (BOARD, WHO'S FIRST, CHOOSE MARKERS X,O)
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? Y or N?: ').upper()

    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    # GAME PLAY

    while game_on:

        if turn == 'Player 1':

            # show board
            display_board(the_board)
            # choose a position
            position = player_choice(the_board)
            # place the marker on the position
            place_marker(the_board, player1_marker, position)
            # check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('PLAYER 1 WON!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            # show board
            display_board(the_board)
            # choose a position
            position = player_choice(the_board)
            # place the marker on the position
            place_marker(the_board, player2_marker, position)
            # check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('PLAYER 2 WON!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break
    # Break out of while loop for replay() function