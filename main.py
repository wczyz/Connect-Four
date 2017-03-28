from graphics import *
from staticValues import *
from settingsWindow import *
from classBoard import *
from functionHumanStrategy import *
from classPlayer import *
import messages

def main():
    """This is the main function"""

    while not settingsWindow.isClosed():
        settingsDraw()


if __name__ == "__main__":
    main()