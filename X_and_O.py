def display_board(board):
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])                                    # creating game board
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])                            # with 9 (numbered) positions
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
test_board=['#','1','2','3','4','5','6','7','8','9']
display_board(test_board)                                                  # display for reference of positions on board

def player_input():
    marker = ''                                                                           # selecting X or O for players
    while not(marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')                                                    # order of X and O as per choice of players
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker                            # placing the markers X and O on selected positions on the board

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or             # all possible winning positions
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))


import random
def choose_first():
    if random.randint(0, 1) == 0:                                             # randomly selecting player for first move
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):
    return board[position] == ' '                                                             # empty space on the board

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):                                                # checking for emty spaces on the board
            return False
    return True

def player_choice(board):
    position=0                                                                          # initial position of board is 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position=int(input('choose ur move (1-9) :'))                             # players choose positions from 1 to 9
    return position


print("WELCOME TO TIC TAC TOE")
while True:
    the_board=[' '] * 10                                                      # displaying board with all spaces cleared
    play_game = input('Ready to play? y or n?')                                           # permission to start the game
    if play_game=='y':
        game_on = True
    else:
        break
    player1_marker, player2_marker = player_input()
    print('1st player: ' + player1_marker)                                           # displaying markers of the players
    print('2nd player: ' + player2_marker)
    turn = choose_first()
    print(turn + ' will go first')                              # displaying player selected for first move to be played
    while game_on==True:
        if turn=='Player 1':                                                                   # for player 1's move and
            display_board(the_board)                                                              # followed by player 2
            position = player_choice(the_board)                                                 # till a winner is found
            place_marker(the_board, player1_marker, position)                                      # or the game is draw
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('player 1 has WON!')
                break
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME')
                    break
                else:
                    turn='Player 2'
        else:
            turn='Player 2'
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('player 2 has WON!')
                break
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    break
                else:
                    turn = 'Player 1'
    ans = input('Do you want to play again?\nYes:y or No:n =>')                   # asking if players want to play again
    if ans == 'y':
        play_game == 'y'                                                          # if yes the game will be played again
    else:
        break                                                                                                 # else END