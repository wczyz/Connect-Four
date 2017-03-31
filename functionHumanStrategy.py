#Function used by the human player object to perform a move

from graphics import *
import messages

def humanStrategy (board):
    """The function for performing the human player's move"""

    win = board.window
    click = None

    # waiting for the player to choose where to move
    while not click:
        click = win.getMouse()
        where = board.checkPosition(click)
        if where != None and board.isValid(where):
            return where;
        else:
            messages.invalidMove(win)
            click = None

    return None;