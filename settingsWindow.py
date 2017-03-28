from graphics import *
from staticValues import *

settingsWindow = GraphWin(WIN_TITLE,SETTINGS_WIDTH,SETTINGS_HEIGHT)
settingsWindow.setBackground("white")

def drawRectangles(p1, p2, colors, n=6):
   """This function draws n coloured rectangles between points p1 and p2 and returns them in a list"""
   dist = abs(p1.getX() - p2.getX()) / n
   rec = []
   x = p1.getX()
   y1 = p1.getY()
   y2 = p2.getY()
   for i in range (n):
       rec.append(Rectangle(Point(x+dist*i,y1),Point(x+dist*(i+1),y2)))
       rec[i].setFill(colors[i])
       rec[i].draw(settingsWindow)
   return rec

def settingsDraw():
    """This function draws settings layout """
    # Title printing
    title = Text(Point(SETTINGS_WIDTH/2, SETTINGS_HEIGHT/10), "CONNECT 4")
    title.setSize(36)
    title.setTextColor("blue")
    title.draw(settingsWindow)

    # "Player1" and "Player2" printing
    playerOneText = Text(Point(SETTINGS_WIDTH/4, SETTINGS_HEIGHT*(3/10)), "PLAYER 1")
    playerOneText.setSize(18)
    playerOneText.draw(settingsWindow)

    playerTwoText = Text(Point(SETTINGS_WIDTH*(3/4), SETTINGS_HEIGHT*(3/10)), "PLAYER 2")
    playerTwoText.setSize(18)
    playerTwoText.draw(settingsWindow)

    # "AI" and "H" buttons
    circle1 = Circle(Point(SETTINGS_WIDTH*(3/16), SETTINGS_HEIGHT*(1/2)), SETTINGS_WIDTH*(1/20))
    circle1.draw(settingsWindow)

    humanText1 = Text(circle1.getCenter(), "H")
    humanText1.setSize(20)
    humanText1.draw(settingsWindow)

    circle2 = Circle(Point(SETTINGS_WIDTH*(5/16), SETTINGS_HEIGHT*(1/2)), SETTINGS_WIDTH*(1/20))
    circle2.draw(settingsWindow)

    aiText1 = Text(circle2.getCenter(), "AI")
    aiText1.setSize(20)
    aiText1.draw(settingsWindow)

    circle3 = Circle(Point(SETTINGS_WIDTH*(11/16), SETTINGS_HEIGHT*(1/2)), SETTINGS_WIDTH*(1/20))
    circle3.draw(settingsWindow)

    humanText2 = Text(circle3.getCenter(), "H")
    humanText2.setSize(20)
    humanText2.draw(settingsWindow)

    circle4 = Circle(Point(SETTINGS_WIDTH*(13/16), SETTINGS_HEIGHT*(1/2)), SETTINGS_WIDTH*(1/20))
    circle4.draw(settingsWindow)

    aiText2 = Text(circle4.getCenter(), "AI")
    aiText2.setSize(20)
    aiText2.draw(settingsWindow)

    # Color boxes
    box1 = drawRectangles(Point(SETTINGS_WIDTH*(1/8), SETTINGS_HEIGHT*(16/20)), Point(SETTINGS_WIDTH*(3/8), SETTINGS_HEIGHT*(14/20)),TOKEN_COLORS)
    box2 = drawRectangles(Point(SETTINGS_WIDTH*(5/8), SETTINGS_HEIGHT*(16/20)), Point(SETTINGS_WIDTH*(7/8), SETTINGS_HEIGHT*(14/20)),TOKEN_COLORS)

    # "GO!" printing
    go = Text(Point(SETTINGS_WIDTH/2, SETTINGS_HEIGHT*(9/10)), "GO!")
    go.setSize(36)
    go.setTextColor("green")
    go.draw(settingsWindow)
