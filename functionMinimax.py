# The function used to perform the minimax search for the AI's strategy.
# Right now the depth of the minimax is constant but eventually progressive deepening will be added.
# TODO: Add alpha-beta prunning and progressive deepening

from staticValues import *
from classBoard import *
from classPlayer import *
from staticValues import *
from functionEvaluation import *
import math
import copy


def minimaxSearch (board, id):
    """Function used to search the game tree further ahead in order to find the best move possible"""

    # This is the position the player is presented with
    start = board

    bestMove = search(start, 0, id - 1)

    return bestMove[1];


def search (node, depth, playerID):
    """A DFS function used to move around the game tree"""

    if playerID % 2 == 0:
        nodeValue = (-float("inf"), None)
    else:
        nodeValue = (float("inf"), None)

    if depth == MAX_DEPTH:
        nodeValue = (evaluation(node), None)
        return nodeValue;

    # Decide whether it's a maximizer's turn or minimizer's
    compare = PLAYER_ROLE[playerID % 2]

    for i in range(node.cols):

        if node.isValid(i):
            move = copy.copy(node)
            move.generateMove(i, playerID + 1)
            childValue = search(move, depth + 1, (playerID + 1) % 2)
            childValue = (childValue[0], i)
            nodeValue = compare(nodeValue, childValue)

    return nodeValue
