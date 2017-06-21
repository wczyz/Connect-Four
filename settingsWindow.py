from graphics import *
from staticValues import *
from functionHumanStrategy import *
from functionAiStrategy import *
import math

settingsWindow = GraphWin(WIN_TITLE,SETTINGS_WIDTH,SETTINGS_HEIGHT)


def settingsDraw():
    """This function draws settings layout and returns chosen options (player strategies and colors)"""


    settingsWindow.setBackground("white")
    playerOneStrategy = humanStrategy
    playerTwoStrategy = aiStrategy
    playerOneColor = TOKEN_COLORS[0]
    playerTwoColor = TOKEN_COLORS[1]

    # Title printing
    title = Text(Point(SETTINGS_WIDTH/2, SETTINGS_HEIGHT/10), "CONNECT 4")
    title.setSize(36)
    title.setTextColor("dark orange")
    title.draw(settingsWindow)

    # "Player1" and "Player2" printing
    playerOneText = Text(Point(SETTINGS_WIDTH/4, SETTINGS_HEIGHT*(2/10)), "PLAYER 1")
    playerOneText.setSize(18)
    playerOneText.draw(settingsWindow)
    playerOneText.setFill(playerOneColor)

    playerTwoText = Text(Point(SETTINGS_WIDTH*(3/4), SETTINGS_HEIGHT*(2/10)), "PLAYER 2")
    playerTwoText.setSize(18)
    playerTwoText.draw(settingsWindow)
    playerTwoText.setFill(playerTwoColor)

    # "AI" and "H" buttons
    circle1 = circleButton(Point(SETTINGS_WIDTH*(3/16), SETTINGS_HEIGHT*(6/20)), SETTINGS_WIDTH*(1/20))
    circle1.draw(settingsWindow)
    circle1.setFill(playerOneColor)
    circle1.setText("H")

    circle2 = circleButton(Point(SETTINGS_WIDTH*(5/16), SETTINGS_HEIGHT*(6/20)), SETTINGS_WIDTH*(1/20))
    circle2.draw(settingsWindow)
    circle2.setText("AI")


    circle3 = circleButton(Point(SETTINGS_WIDTH*(11/16), SETTINGS_HEIGHT*(6/20)), SETTINGS_WIDTH*(1/20))
    circle3.draw(settingsWindow)
    circle3.setText("H")

    circle4 = circleButton(Point(SETTINGS_WIDTH*(13/16), SETTINGS_HEIGHT*(6/20)), SETTINGS_WIDTH*(1/20))
    circle4.draw(settingsWindow)
    circle4.setFill(playerTwoColor)
    circle4.setText("AI")

    # printing color boxes
    box1 = drawRecButtons(Point(SETTINGS_WIDTH*(1/8), SETTINGS_HEIGHT*(5/10)), Point(SETTINGS_WIDTH*(3/8), SETTINGS_HEIGHT*(4/10)),TOKEN_COLORS)
    box2 = drawRecButtons(Point(SETTINGS_WIDTH*(5/8), SETTINGS_HEIGHT*(5/10)), Point(SETTINGS_WIDTH*(7/8), SETTINGS_HEIGHT*(4/10)),TOKEN_COLORS)

    # printing input boxes with text
    # TODO: set maximal and minimal values for rows and cols?

    rows_entry = Entry(Point(SETTINGS_WIDTH*(55/100),SETTINGS_HEIGHT*(6/10)),2)
    rows_entry.setText(DEFAULT_ROWS)
    rows_entry.draw(settingsWindow)
    rows_text = Text(Point(SETTINGS_WIDTH*(49/100),SETTINGS_HEIGHT*(6/10)), "Number of rows:")
    rows_text.draw(settingsWindow)

    cols_entry = Entry(Point(SETTINGS_WIDTH * (55/100), SETTINGS_HEIGHT * (13 / 20)), 2)
    cols_entry.setText(DEFAULT_COLS)
    cols_entry.draw(settingsWindow)
    cols_text = Text(Point(SETTINGS_WIDTH * (49 / 100), SETTINGS_HEIGHT * (13 / 20)), "Number of cols:")
    cols_text.draw(settingsWindow)

    # "Play button" printing
    play = recButton(Point(SETTINGS_WIDTH*(7/16), SETTINGS_HEIGHT*(15/20)),Point(SETTINGS_WIDTH*(9/16), SETTINGS_HEIGHT*(17/20)))
    play.draw(settingsWindow)
    play.setFill("dark orange")
    tri = Polygon(Point(play.x1+play.width/3,play.y1+play.height/5),Point(play.x1+play.width/3,play.y1+play.height*(4/5)),Point(play.x1+play.width*(2/3),play.y1+play.height/2))
    tri.draw(settingsWindow)
    tri.setFill("black")



    #checking if any of the objects are clicked
    while not settingsWindow.isClosed():
        click = settingsWindow.getMouse()
        if (circle1.isClicked(click)):
            circle1.setFill(playerOneColor)
            circle2.setFill(BACKGROUND_COLOR)
            playerOneStrategy = humanStrategy

        if (circle2.isClicked(click)):
            circle2.setFill(playerOneColor)
            circle1.setFill(BACKGROUND_COLOR)
            playerOneStrategy = aiStrategy

        if (circle3.isClicked(click)):
            circle3.setFill(playerTwoColor)
            circle4.setFill(BACKGROUND_COLOR)
            playerTwoStrategy = humanStrategy

        if (circle4.isClicked(click)):
            circle4.setFill(playerTwoColor)
            circle3.setFill(BACKGROUND_COLOR)
            playerTwoStrategy = aiStrategy

        for i in box1:
            if (i.isClicked(click)):
                if (playerTwoColor != i.color):
                    playerOneText.setFill(i.color)
                    playerOneColor = i.color
                    if(playerOneStrategy == humanStrategy):
                        circle1.setFill(i.color)
                    else:
                        circle2.setFill(i.color)

        for i in box2:
            if (i.isClicked(click)):
                if(playerOneColor != i.color):
                    playerTwoText.setFill(i.color)
                    playerTwoColor = i.color
                    if(playerTwoStrategy == humanStrategy):
                        circle3.setFill(i.color)
                    else:
                        circle4.setFill(i.color)

        if(play.isClicked(click)):
            rows = int(rows_entry.getText())
            cols = int(cols_entry.getText())
            settingsWindow.close()

    return(playerOneStrategy, playerOneColor, playerTwoStrategy, playerTwoColor, rows, cols)




def dist(p1,p2):
    """returns distance between 2 points"""

    x = p1.getX() - p2.getX()
    y = p1.getY() - p2.getY()
    return math.hypot(x, y)

def drawRecButtons(p1, p2, colors, n=6):
   """This function draws n coloured rectangle buttons between points p1 and p2 and returns them in a list"""
   dist = abs(p1.getX() - p2.getX()) / n
   rec = []
   x = p1.getX()
   y1 = p1.getY()
   y2 = p2.getY()
   for i in range (n):
       rec.append(recButton(Point(x+dist*i,y1),Point(x+dist*(i+1),y2)))
       rec[i].setFill(colors[i])
       rec[i].draw(settingsWindow)
   return rec

class circleButton:
    def __init__(self, center, r):
        """Constructor setting the centre of the circle with its diameter r"""

        self.center = center
        self.r = r
        self.circle = Circle(center,r)
        self.textObj = None
        self.window = None

    def draw(self, window):
        """Method used to draw the button in the given window"""

        self.window = window
        self.circle.draw(self.window)
        if (self.textObj):
            self.textObj.draw(self.window)

    def undraw(self, window):
        """Method used to undraw the button in the given window"""

        self.window = window
        self.circle.undraw()
        self.textObj.undraw()

    def setFill(self, color):
        """Method filling the button with given color (if a text is set, it draws it again on the button)"""

        self.color = color
        if (self.textObj):
            self.textObj.undraw()
        self.circle.setFill(self.color)
        if (self.textObj):
            self.textObj.draw(self.window)

    def setText(self, text):
        """Method drawing the given text inside the button"""
        self.textObj = Text(self.center,text)
        self.textObj.setSize(20)
        self.textObj.draw(self.window)


    def isClicked(self,click):
        """Method returns True if the button was recently clicked"""

        if not click:
            return None
        d = dist(click, self.center)
        if(d<self.r):
            return True
        else:
            return False

class recButton:
    def __init__(self, p1, p2):
        """Constructor setting the two opposing points of the rectangle along with its color"""

        self.p1 = p1
        self.x1 = p1.getX()
        self.y1 = p1.getY()
        self.p2 = p2
        self.x2 = p2.getX()
        self.y2 = p2.getY()
        self.rec = Rectangle(p1,p2)
        self.color = None
        self.window = None
        self.width = abs(self.x2-self.x1)
        self.height = abs(self.y1-self.y2)

    def draw(self, window):
        """Method used to draw the button onto the given window"""

        self.window = window
        self.rec.draw(window)

    def setFill(self, color):
        """Method filling the button with given color"""

        self.color = color
        self.rec.setFill(self.color)

    def isClicked(self, click):
        """Method returns True if the button was recently clicked"""

        if not click:
            return None
        x = click.getX()
        y = click.getY()
        xLeft = min(self.x1,self.x2)
        xRight = max(self.x1,self.x2)
        yUp = min(self.y1,self.y2)
        yDown = max(self.y1,self.y2)
        if(x>xLeft and x<xRight and y>yUp and y<yDown):
            return True
        else:
            return False
