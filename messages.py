#Namespace containing all the messages and errors used in the program

from graphics import *

def invalidMove (window):
    """Function shows the message when the invalid move is being chosen"""

    print("INVALID MOVE!")

def gameOver (window, id):
    """Function shows the message when the game is won by any player or drawn"""

    if id == 0:
        print("DRAW")
    else
        print("PLAYER {} HAS WON!".format(id))