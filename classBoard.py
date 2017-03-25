from graphics import *

class Board:

    def __init__(self, rows, columns):
        #MARK: variables
        
        self.boxSize = 71
        self.backgroundColor = "white"
        self.playerOneColor = "red"
        self.playerTwoColor = "blue"
        self.windowWeight = rows*boxSize + rows - 1
        self.windowHeight = columns*boxSize + columns - 1

        #MARK: build window
        self.window = GraphWin("Connect Four", windowWeight, windowHeight)
        window.setBackground(backGroundColor)

        for i in range(boxSize+1, windowWeight+1, boxSize+1):
            yLine = Line(Point(i, 0), Point(i, windowHeight))
            yLine.draw(window)

        for i in range(boxSize+1, windowHeight+1, boxSize+1):
            xLine = Line(Point(0, i), Point(windowWeight, i))
            xLine.draw(window)

        #MARK: Conteiners

        self.boxStatus = [0] * (rows*columns) # 0 - empty, 1 - first player, 2 - second player

        self.boxCircles = [None] * (rows*columns)

        window.getMouse()


    def updateBox(self, coordinateX, coordinateY, status):
        boxNumber = (coordinateY-1) * columns + coordinateX - 1

        if(boxCircles[boxNumber] == None):
            boxCircles[boxNumber] = Circle(Point((coordinateX-1)*(boxSize+1) + boxSize//2 + 1, (coordinateY-1)*(boxSize+1 + boxSize//2 + 1)), boxSize//2)
            if(status == 1):
                boxCircles[boxNumber].setFill(playerOneColor)
            else:
                boxCircles[boxNumber].setFill(playerTwoColor)
            boxCircles[boxNumber].draw(window)
        else:
            boxCircle[boxNumber].undraw(window)
            boxCircle[boxNumber] = None;



def main():
    zmienna = Board(9, 10)
    zmienna.updateBox(2, 2, 1)

main()