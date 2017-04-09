from graphics import *
from staticValues import *
from settingsWindow import *
from classBoard import *
from functionHumanStrategy import *
from functionAiStrategy import *
from functionEvaluation import *
from classPlayer import *
import messages

def main():
    """This is the main function"""

    playerOneStrategy, playerOneColor, playerTwoStrategy, playerTwoColor = settingsDraw()

    # Temporary input
    rows = int(input("rows: "))
    cols = int(input("columns: "))

    # Testing the gameplay

    width = min(cols*100, MAX_WIDTH)
    height = (width / cols) * rows
    gameWindow = GraphWin("Connect Four", width, height)
    gameWindow.setBackground("white")
    gameWindow.setCoords(0, 0, width, height)
    board = Board(rows, cols, gameWindow, width, height)
    board.draw()
    player1 = Player(1, playerOneColor, playerOneStrategy, board)
    player2 = Player(2, playerTwoColor, playerTwoStrategy, board)
    while not gameWindow.isClosed():
        # TODO: Maybe move the isOver check to the move() function
        player1.move()
        if board.isOver():
            break

        player2.move()
        if board.isOver():
            break

    gameWindow.close()


if __name__ == "__main__":
    main()
