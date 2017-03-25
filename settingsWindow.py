from graphics import *
from staticValues import *

settingsWindow = GraphWin(WIN_TITLE,SETTINGS_WIDTH, SETTINGS_HEIGHT)

# def drawRectangles(a, b, c=6):
#    """This function draws c rectangles between points a and b """
#    dist = abs(a.getX - b.getX) / c
#
#    rec = []


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
    #drawRectangles(Point(SETTINGS_WIDTH*(1/8)), SETTINGS_HEIGHT*(16/20), Point(SETTINGS_WIDTH*(3/8), SETTINGS_HEIGHT*(14/20)))
    #drawRectangles(Point(SETTINGS_WIDTH*(5/8)), SETTINGS_HEIGHT*(16/20), Point(SETTINGS_WIDTH*(7/8), SETTINGS_HEIGHT*(14/20)))
    # "GO!" printing
    go = Text(Point(SETTINGS_WIDTH/2, SETTINGS_HEIGHT*(9/10)), "GO!")
    go.setSize(36)
    go.setTextColor("green")
    go.draw(settingsWindow)
