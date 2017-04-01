#Function used by the AI player object to perform a move

from staticValues import *
from classBoard import *
from classPlayer import *

def sumOfPoints(board, player):

    points = 0
    #For every free position check how many free tokens are availeable in every direction
    for i in range(board.cols):
        y = board.columnSize[i]
        x = i
        if(y < board.rows):
            #horizontally
            a = 0
            for j in range(1,4):
                x+=1
                if(x>=board.cols):
                    break
                if(board.container[y*board.cols + x] == player.id):
                    a+=1
                else:
                    break

            x = i

            for j in range(1,4):
                x-=1
                if(x<0):
                    break
                if(board.container[y*board.cols + x] == player.id):
                    a+=1
                else:
                    break

            #print("Horizontally: " + str(a))

            points += EVALUATION[min(a,3)]

            x = i

            #vertically
            a=0
            for j in range(1,4):
                y+=1
                if(y>=board.rows):
                    break
                if(board.container[y*board.cols + x] == player.id):
                    a+=1
                else:
                    break

            y = board.columnSize[i]

            for j in range(1,4):
                y-=1
                if(y<0):
                    break
                if(board.container[y*board.cols + x] == player.id):
                    a+=1
                else:
                    break

            y = board.columnSize[i]

            #print("Vertically " + str(a))

            points += EVALUATION[min(a,3)]

            #diagonally 1
            a=0
            x = i
            y = board.columnSize[i]

            for j in range(1,4):
                x+=1
                y+=1
                if(x>=board.cols or y>=board.rows):
                    break
                if(board.container[y*board.cols + x] == player.id):
                    a+=1
                else:
                    break

            x = i
            y = board.columnSize[i]

            for j in range(1,4):
                x-=1
                y-=1
                if(x<0 or y<0):
                    break
                if(board.container[y*board.cols + x] == player.id):
                    a+=1
                else:
                    break

            #print("Diagonally1: " + str(a))

            points += EVALUATION[min(a,3)]

            #diagonally 2
            a=0

            x = i
            y = board.columnSize[i]

            for j in range(1,4):
                x-=1
                y+=1
                if(x<0 or y>=board.rows):
                    break
                if(board.container[y*board.cols + x] == player.id):
                    a+=1
                else:
                    break

            x = i
            y = board.columnSize[i]

            for i in range(1,4):
                x+=1
                y-=1
                if(x>=board.cols or y<0):
                    break
                if(board.container[y*board.cols + x] == player.id):
                    a+=1
                else:
                    break

            #print("Diagonally2: " + str(a))

            points += EVALUATION[min(a,3)]

    return points

def aiStrategy(board, player1, player2):
    return sumOfPoints(board,player1) - sumOfPoints(board,player2)
