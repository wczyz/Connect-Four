#Function used by the AI player object to perform a move

from staticValues import *
from classBoard import *
from classPlayer import *
from functionMinimax import *
import random

def aiStrategy (board, id):
    """The function for performing the computer player's move"""

    return minimaxSearch(board, id);