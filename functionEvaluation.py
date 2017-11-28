# Function used to evaluate some given state of the board

from staticValues import *
from classBoard import *
from classPlayer import *

def isThere(board, x, y, player):
    """This function states whether player's token is at position (x,y)."""
    if(board.container[y * board.cols + x] == player):
        return True
    else:
        return False

def sumOfPoints(board, player):

    points = 0

    #Vertically

    for i in range(board.cols):
        a = 0
        for j in range(board.rows):
            if(isThere(board, i, j, player)):
                a += 1
            else:
                points+=EVALUATION[min(a, board.goal)]
                a = 0
        points+=EVALUATION[min(a, board.goal)]

    #Horizontally

    for i in range(board.rows):
        a = 0
        for j in range(board.cols):
            if(isThere(board, j, i, player)):
                a += 1
            else:
                points += EVALUATION[min(a, board.goal)]
                a = 0
            points += EVALUATION[min(a, board.goal)]

    #Diagonally 1

    for i in range(board.rows-1, 0, -1):
        a = 0
        for j in range(board.rows - i):
            if(isThere(board, j, i+j, player)):
                a += 1
            else:
                points += EVALUATION[min(a, board.goal)]
                a = 0
            points += EVALUATION[min(a, board.goal)]

    for i in range(board.cols):
        a = 0
        for j in range(min(board.rows,board.cols-i)):
            if(isThere(board, i+j, j, player)):
                a += 1
            else:
                points += EVALUATION[min(a, board.goal)]
                a = 0
            points += EVALUATION[min(a, board.goal)]

    #Diagonally 2

    for i in range(board.cols):
        a = 0
        for j in range(min(board.rows, i+1)):
            if(isThere(board, i-j, j, player)):
                a += 1
            else:
                points += EVALUATION[min(a, board.goal)]
                a = 0
            points += EVALUATION[min(a, board.goal)]

    for i in range(1, board.rows):
        a = 0
        for j in range(board.rows-i):
            if(isThere(board, board.cols-1-j, i+j, player)):
                a += 1
            else:
                points += EVALUATION[min(a, board.goal)]
                a = 0
            points += EVALUATION[min(a, board.goal)]

    return points

def evaluation(board, depth):
    return (MAX_DEPTH - depth + 1) * (sumOfPoints(board, 1) - sumOfPoints(board, 2))
