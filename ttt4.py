import os
import random

board = [' ' for i in range(16)]
computer = 'x'
human = 'o'
player = human
win_data = [
    [ 0,  1,  2,  3], [ 4,  5,  6,  7], [ 8,  9, 10, 11], [12, 13, 14, 15],
    [ 0,  4,  8, 12], [ 1,  5,  9, 13], [ 2,  6, 10, 14], [ 3,  7, 11, 15],
    [ 0,  5, 10, 15], [ 3,  6,  9, 12]
]


def print_board():
    os.system('clear')
    print(f'\n {board[0]} | {board[1]} | {board[2]} | {board[3]}')
    print('---+---+---+---')
    print(f' {board[4]} | {board[5]} | {board[6]} | {board[7]}')
    print('---+---+---+---')
    print(f' {board[8]} | {board[9]} | {board[10]} | {board[11]}')
    print('---+---+---+---')
    print(f' {board[12]} | {board[13]} | {board[14]} | {board[15]}\n')


def make_move():
    if player == human:
        while True:
            try:
                position = int(input('Enter position (0-15): '))
                
                if position == 100:
                    return 100
                elif position >= 0 and position <= 15:
                    if board[position] == ' ':
                        board[position] = player
                        return position
                    else:
                        print('Position already taken!')
                else:
                    print('Invalid position!')
            except:
                print('Please type a number!')
    else:
        move = computer_move()
        board[move] = player
        return move


def computer_move():
    available_position = [i for i in range(16) if board[i] == ' ']
    
    # try to win
    for i in available_position:
        board[i] = computer
        if is_win() == computer:
            board[i] = ' '
            return i
        board[i] = ' '
    
    # try to block
    for i in available_position:
        board[i] = human
        if is_win() == human:
            board[i] = ' '
            return i
        board[i] = ' '
    
    return random.choice(available_position)


def is_win():
    for win in win_data:
        if all(board[i] == computer for i in win):
            return computer
        if all(board[i] == human for i in win):
            return human
    return None


def is_draw():
    return ' ' not in board


def switch_player():
    global player
    
    if player == human:
        player = computer
    else:
        player = human
    
    return player


def main():
    while True:
        print_board()
        move= make_move()
        
        if move == 100:
            break
        
        result = is_win()
        if result == player:
            print_board()
            print(f'Player ({result}) win!')
            break
        
        if is_draw():
            print_board()
            print('It\'s a tie!')
            break
        
        switch_player()


main()