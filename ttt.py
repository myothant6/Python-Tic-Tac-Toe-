import os
import random

board = [' ' for i in range(9)]
human = 'o'
computer = 'x'
player = human
win_data = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]

def print_board():
    os.system('clear')
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('---+---+---')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('---+---+---')
    print(f' {board[6]} | {board[7]} | {board[8]} ')


def minmax(maximize, depth):
    result = win()
    if result == computer: return 10 - depth
    elif result == human: return depth - 10
    elif draw(): return 0
    elif depth == 100: return 0

    if maximize:
        best_score = -100
        for i in range(9):
            if board[i] == ' ':
                board[i] = computer
                score = minmax(False, depth + 1)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = 100
        for i in range(9):
            if board[i] == ' ':
                board[i] = human
                score = minmax(True, depth + 1)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score


def computer_move():
    available_position = [i for i in range(9) if board[i] == ' ']
    best_score = -100
    best_moves = []

    for i in available_position:
        board[i] = computer
        score = minmax(False, 0)
        board[i] = ' '

        if score > best_score:
            best_score = score
            best_moves = [i]   # reset list
        elif score == best_score:
            best_moves.append(i)  # add more choices

    return random.choice(best_moves)


def make_move():
    if player == human:
        while True:
            position = int(input('Enter position (0-8): '))
            if position >= 0 and position <= 8:
                if board[position] == ' ':
                    board[position] = player
                    break
                else:
                    print('Position already taken.')
            else:
                print('Type error.')
    else:
        board[computer_move()] = computer
    
    switch()


def switch():
    global player
    
    if player == human:
        player = computer
    else:
        player = human


def draw(): return ' ' not in board


def win():
    for w in win_data:
        if all(board[i] == human for i in w):
            return human
        if all(board[i] == computer for i in w):
            return computer
    return False


def main():
    while True:
        print_board()
        make_move()
        
        result = win()
        if result:
            print_board()
            print(f'Player ({result}) win!')
            break
        
        if draw():
            print_board()
            print('Draw')
            break

main()
