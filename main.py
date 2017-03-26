from graphics import *
from staticValues import *
from settingsWindow import *

def main():
    """This is the main function"""

    while not settingsWindow.isClosed():
        settingsDraw()


main()
