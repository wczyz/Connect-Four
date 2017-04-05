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

    # while not settingsWindow.isClosed():
    #     settingsDraw()

    # Temporary input
    rows = int(input("rows: "))
    cols = int(input("columns: "))

    # Testing the gameplay
    # TODO: Set the player type according to the decisions made in settingsWindow
    width = min(cols*100, MAX_WIDTH)
    height = (width / cols) * rows
    gameWindow = GraphWin("Connect Four", width, height)
    gameWindow.setBackground("white")
    gameWindow.setCoords(0, 0, width, height)
    board = Board(rows, cols, gameWindow, width, height)
    board.draw()
    player1 = Player(1, "red", aiStrategy, board)
    player2 = Player(2, "blue", aiStrategy, board)
    while not gameWindow.isClosed():
        # TODO: Maybe move the isOver check to the move() function
        player1.move()
        if board.isOver():
            break
        #debug
        print(evaluation(board))

        player2.move()
        if board.isOver():
            break

    gameWindow.close()


if __name__ == "__main__":
    main()
