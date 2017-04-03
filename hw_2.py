import numpy as np
import random
def create_board():
    return np.zeros((3,3))

def place(board, player, position):
    if board[position] == 0:
        board[position] = player


board = create_board()
place(board, 1, (0, 0))

def possibilities(board):
    return list(zip(np.where(board == 0)[0], np.where(board == 0)[1]))

#print(possibilities(board))

def random_place(board,player):
    position=random.choice(possibilities(board))
    place(board,player,position)

random_place(board,2)

for i in range(3):
    for player in [1, 2]:
        random_place(board,player)

print(board)

def row_win(board, player):
    for row in board:
        if np.array_equal(row,np.full(3,player)):
            return True
    return False

print(row_win(board,1))

def col_win(board, player):
    for col in board.T:
        if np.array_equal(col,np.full(3,player)):
            return True
    return False

print(col_win(board,1))

def diag_win(board, player):
    if (board[0,0]==player and board[1,1]==player and board[2,2]==player) or (board[2,0]==player and board[1,1]==player and board[0,2]==player):
        return True
    return False

print(diag_win(board,1))

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        # Check if `row_win`, `col_win`, or `diag_win` apply.  if so, store `player` as `winner`.
        if row_win(board,player) or col_win(board,player) or diag_win(board,player):
            return player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

print(evaluate(board))

def play_game():
    board = create_board()
    while True:
        for player in [1,2]:
            random_place(board,player)
            check=evaluate(board)
            if check!=0:
                #print(board)
                return check

print(play_game())

import time
import matplotlib.pyplot as plt
start=time.time()

results=[]
for i in range(0,1000):
    results.append(play_game())

plt.hist(results)
plt.show()

end=time.time()
print(end-start)

def play_strategic_game():
    board, winner = create_board(), 0
    board[1,1] = 1
    while winner == 0:
        for player in [2,1]:
            random_place(board,player)
            winner=evaluate(board)
            if winner != 0:
                break
    return winner

print(play_strategic_game() )

start=time.time()

results=[]
for i in range(0,1000):
    results.append(play_strategic_game())

plt.hist(results)
plt.show()

end=time.time()
print(end-start)