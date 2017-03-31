# Board class, representing the game board with all the needed update methods

from graphics import *
from classPlayer import *
import messages

class Board:

    def __init__ (self, row, col, win, winWidth, winHeight, goal = 4):
        """Constructor setting the size of the board and a pointer to the game window along with all other aspects
        of the game.

        An empty board is created with no tokens on it."""

        self.rows = row
        self.cols = col
        self.boxSize = winHeight / row
        self.window = win
        self.height = winHeight
        self.width = winWidth
        self.size = row*col
        self.goal = goal # The number of tokens in a row needed to win
        self.status = -1 # It keeps track of whether the game is over or not, -1 being not over and {0, 1, 2} being
                         #      a draw and the first and second player's win respectively
        self.tokens = [None for i in range(self.size)] # list of all the tokens as graphical objects
        self.container = [0 for i in range(self.size)] # List representing the situation on the board,
                                                       # 0 - no token, 1 - first player, 2 - second player
        self.columnSize = [0 for i in range(self.cols)] # List containing the number of tokens in each column


    def update (self, where, player):
        """Method used to update the board according to a given move"""

        x = (where % self.cols) * self.boxSize + (self.boxSize / 2)
        y = (where // self.cols) * self.boxSize + (self.boxSize / 2)

        self.tokens[where] = Circle(Point(x, y), (self.boxSize / 2) - 5)
        self.tokens[where].setFill(player.tokenColor)

        # TODO: Write an animation loop for the token
        # while not onTheBottom:
        #     animation()

        self.statusUpdate(where, player.id)
        self.columnSize[where % self.cols] += 1
        self.container[where] = player.id
        self.tokens[where].draw(self.window)



    def draw (self):
        """Method used to draw the grid and all of the tokens"""

        for token in self.tokens:
            if token:
                token.undraw()
                token.draw(self.window)

        # # Drawing the frame, TODO: Apply some wooden/plastic texture
        # frame = Rectangle(Point(0, 0), Point(self.width, self.height))
        # frame.setFill("brown2")
        # frame.draw(self.window)

        # Drawing the grid
        # Horizontal lines
        i = 0
        while i <= self.height:
            line = Line(Point(0, i), Point(self.width, i))
            # line.setWidth(2)
            line.draw(self.window)
            i += self.boxSize
        # Vertical lines
        i = 0
        while i <= self.height:
            line = Line(Point(i, 0), Point(i, self.height))
            # line.setWidth(2)
            line.draw(self.window)
            i += self.boxSize


    def checkPosition (self, click):
        """Method used to define the index in the container list based on the given mouse click coordinates.

        Parameter 'click' is a Point object.
        It returns the index in a normalized 1D list"""

        if not click:
            return None;

        x = click.getX() // self.boxSize
        y = self.columnSize[int(x)]

        return int(y*self.cols + x);


    def isValid (self, where):
        """Method checks if the given move can be performed on this board."""

        x = where % self.cols

        return self.columnSize[x] < self.rows;


    def statusUpdate (self, where, id):
        """Method used to check whether the game is over or not."""

        playerID = id

        # Horizontal tokens check
        a = (where // self.cols) * self.cols
        b = a + self.cols
        counter = 1
        for i in range(where + 1, b):
            if self.container[i] != playerID:
                break
            counter += 1
        for i in range(where - 1, a - 1, -1):
            if self.container[i] != playerID:
                break
            counter += 1

        if counter >= self.goal:
            self.status = playerID
            return;

        # Vertical tokens check
        a = 0
        b = self.size
        counter = 1
        for i in range(where + self.cols, b, self.cols):
            if self.container[i] != playerID:
                break
            counter += 1
        for i in range(where - self.cols, a - 1, -self.cols):
            if self.container[i] != playerID:
                break
            counter += 1

        if counter >= self.goal:
            self.status = playerID
            return;

        # Diagonal tokens check
        b = self.size
        x = int(where % self.cols)

        counter = 1
        pos = where + (self.cols - 1)
        for i in range(x):
            if pos >= self.size:
                break
            if self.container[pos] != playerID:
                break
            pos += (self.cols - 1)
            counter += 1
        pos = where - (self.cols - 1)
        for i in range(self.cols - x - 1):
            if pos < 0:
                break
            if self.container[pos] != playerID:
                break
            pos -= (self.cols - 1)
            counter += 1

        if counter >= self.goal:
            self.status = playerID
            return;

        counter = 1
        pos = where + (self.cols + 1)
        for i in range(self.cols - x - 1):
            if pos >= self.size:
                break
            if self.container[pos] != playerID:
                break
            pos += (self.cols + 1)
            counter += 1
        pos = where - (self.cols + 1)
        for i in range(x):
            if pos < 0:
                break
            if self.container[pos] != playerID:
                break
            pos -= (self.cols + 1)
            counter += 1

        if counter >= self.goal:
            self.status = playerID
            return;

        # Check if the given move results in a draw
        counter = 1
        for i in self.columnSize:
            counter += i
        if counter >= self.size:
            self.status = 0


    def isOver (self):
        """Method returns True if the game on this board is drawn or won and False otherwise."""

        if self.status == -1:
            return False;

        messages.gameOver(self.window, self.status)
        self.window.getMouse()

        return True;


    def longestChain (self):
        """Method returning the longest chain of the same tokens on the board."""

        # TODO: Implement this method and decide whether it should take player's number as a parameter
        # TODO: or return the longest chain on the board with the number representing to whom it belongs


# THE DEBUG SECTION
if __name__ == "__main__":
    win = GraphWin("DEBUG", 700, 600)
    win.setCoords(0, 0, 700, 600)
    b = Board(6, 7, win, 600, 700)
    b.draw()
    while not win.isClosed():
        c = win.getMouse()
        w = b.checkPosition(c)
        print(b.update(w, None))
