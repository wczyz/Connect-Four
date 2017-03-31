#Player class, used for both human and computer

from graphics import *

class Player:

    def __init__ (self, playerID, tokenColor, strategy, board):
        """Constructor setting the given color of the player's tokens and theirs strategy.
        It also sets a pointer to the board on which the current game is played.

        Strategy can be either a human move function or AI's strategy."""

        self.tokenColor = tokenColor
        self.strategy = strategy
        self.board = board
        self.id = playerID


    def move (self):
        """Method launching the strategy function of the player object"""

        whereToMove = self.strategy(self.board)

        # Updating the board
        self.board.update(whereToMove, self)
