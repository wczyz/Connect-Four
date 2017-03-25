from graphics import *

class Board:

    def __init__(self, ROWS, COLUMNS):
        #MARK: variables
        boxSize = 71
        backGroundColor = "white"
        windowWeight = ROWS*boxSize+ROWS-1
        windowHeight = COLUMNS*boxSize+COLUMNS-1

        #MARK: build window
        window = GraphWin("Connect Four", windowWeight, windowHeight)
        window.setBackground(backGroundColor)

        for i in range(boxSize+1, windowWeight+1, boxSize+1):
            yLine = Line(Point(i, 0), Point(i, windowHeight))
            yLine.draw(window)

        for i in range(boxSize+1, windowHeight+1, boxSize+1):
            xLine = Line(Point(0, i), Point(windowWeight, i))
            xLine.draw(window)

        #MARK: Conteiners

        boxStatus = [0] * (ROWS*COLUMNS) # 0 - empty, 1 - first player, 2 - second player

        boxCircles = [None] * (ROWS*COLUMNS)

        window.getMouse()






def main():
    zmienna = Board(9, 10)
main()