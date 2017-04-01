from graphics import *
from staticValues import *
from settingsWindow import *
from classBoard import *
from functionHumanStrategy import *
from functionAiStrategy import *
from classPlayer import *
import messages

def main():
    """This is the main function"""

    # while not settingsWindow.isClosed():
    #     settingsDraw()

    # Testing for the two human players
    # TODO: Set the player type according to the decisions made in settingsWindow
    gameWindow = GraphWin("Connect Four", 700, 600)
    gameWindow.setCoords(0, 0, 700, 600)
    board = Board(6, 7, gameWindow, 700, 600)
    board.draw()
    player1 = Player(1, "red", humanStrategy, board)
    player2 = Player(2, "blue", humanStrategy, board)
    while not gameWindow.isClosed():
        # TODO: Maybe move the isOver check to the move() function
        player1.move()
        if board.isOver():
            break
        #debug
        print(aiStrategy(board,player1,player2))

        player2.move()
        if board.isOver():
            break

    gameWindow.close()


if __name__ == "__main__":
    main()
