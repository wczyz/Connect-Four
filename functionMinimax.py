# The function used to perform the minimax search for the AI's strategy.
# Right now the depth of the minimax is constant but eventually progressive deepening will be added.
# Alpha-beta pruning has been implemented to reduce the number of branches checked in the tree
# TODO: Add progressive deepening and some way of sorting the child nodes

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

    bestMove = search(start, 0, id - 1, -float("inf"), float("inf"))

    return bestMove[1];


def search (node, depth, playerID, alpha, beta):
    """A DFS function used to move around the game tree"""

    if playerID % 2 == 0:
        nodeValue = (-float("inf"), -node.cols)
    else:
        nodeValue = (float("inf"), node.cols)

    if depth == MAX_DEPTH:
        nodeValue = (evaluation(node), nodeValue[1])
        return nodeValue;

    # Decide whether it's a maximizer's turn or minimizer's
    compare = PLAYER_ROLE[playerID % 2]

    for i in range(node.cols):

        if node.isValid(i):
            move = copy.copy(node)
            move.generateMove(i, playerID + 1)
            childValue = search(move, depth + 1, (playerID + 1) % 2, alpha, beta)
            childValue = (childValue[0], i)
            nodeValue = compare(nodeValue, childValue)

            # Updating the alpha-beta guards
            if playerID % 2 == 0:
                alpha = compare(alpha, nodeValue[0])
            else:
                beta = compare(beta, nodeValue[0])

            # Checking if possible to prune
            if beta <= alpha:
                break

    return nodeValue
