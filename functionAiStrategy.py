#Function used by the AI player object to perform a move

from staticValues import *
from classBoard import *
from classPlayer import *
import random

def aiStrategy (board):
    """The function for performing the computer player's move"""

    move = random.randint(0, board.cols - 1)

    while not board.isValid(move):
        move = random.randint(0, board.cols - 1)

    return move;