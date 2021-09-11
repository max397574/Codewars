#https://www.codewars.com/kata/525caa5c1bf619d28c000335/train/python
import numpy as np
def is_solved(board):
    board=np.array(board)
    if board[0,0]==board[0,1]==board[0,2]==1:
        return 1
    if board[0,0]==board[0,1]==board[0,2]==2:
        return 2
    if board[1,0]==board[1,1]==board[1,2]==1:
        return 1
    if board[1,0]==board[1,1]==board[1,2]==2:
        return 2
    if board[2,0]==board[2,1]==board[2,2]==1:
        return 1
    if board[2,0]==board[2,1]==board[2,2]==2:
        return 2
    if board[0,0]==board[1,0]==board[2,0]==1:
        return 1
    if board[0,1]==board[1,1]==board[2,1]==1:
        return 1
    if board[0,2]==board[1,2]==board[2,2]==1:
        return 1
    if board[0,0]==board[1,0]==board[2,0]==2:
        return 2
    if board[0,1]==board[1,1]==board[2,1]==2:
        return 2
    if board[0,2]==board[1,2]==board[2,2]==2:
        return 2
    if board[0,0]==board[1,1]==board[2,2]==1:
        return 1
    if board[2,0]==board[1,1]==board[0,2]==1:
        return 1
    if board[0,0]==board[1,1]==board[2,2]==2:
        return 2
    if board[2,0]==board[1,1]==board[0,2]==2:
        return 2
    if 0 in board:
        return -1
    return 0


board=[[0,0,1],
        [2,2,2],
        [1,2,1]]
if is_solved(board)==1:
    print("X won")
elif is_solved(board)==2:
    print("O won")
elif is_solved(board)==-1:
    print("the game isn't finished yet")
elif is_solved(board)==0:
    print("draw")
