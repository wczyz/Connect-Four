WIN_TITLE = "Connect Four"
SETTINGS_WIDTH = 1200
SETTINGS_HEIGHT = 800
MAX_WIDTH = 1080 # maximum width of the game window
# MAX_HEIGHT = 800
TOKEN_COLORS = ('crimson','midnight blue','royal blue','olive','lime green','goldenrod')
BACKGROUND_COLOR = 'white'
EVALUATION = [1, 5, 20, 5000, 100000000] # the values used for static evaluation
PLAYER_ROLE = [max, min] # list storing the functions used by players in a minimax search,
                         # 1st player is a maximizer and 2nd is a minimizer
MAX_DEPTH = 5 # temporary value indicating the maximum depth of the minimax tree
