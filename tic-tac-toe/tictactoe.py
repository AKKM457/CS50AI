"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x = 0
    o = 0

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == X:
                x+=1
            elif board[i][j] == O:
                o+=1
    if x > o:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    m = set()

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                m.add((i,j))
    return m


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if action not in actions(board):
        raise Exception("Invalid Move")

    x, y = action
    b = copy.deepcopy(board)
    b[x][y] = player(board)

    return b

def checkR(board, player):


    for i in range(len(board)):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True

    return False

def checkC(board, player):

    for j in range(len(board)):
        if board[0][j] == player and board[1][j] == player and board[2][j] == player:
            return True

    return False

def checkD(board, player):

    c = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if i == j and board[i][j] == player:
                c+=1

    if c == 3:
        return True
    else:
        return False

def checkD2(board, player):

     c = 0

     for i in range(len(board)):
         for j in range(len(board[i])):
             if (len(board) - i - 1) == j and board[i][j] == player:
                 c+=1
     if c == 3:
         return True
     else:
         return False

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if checkD(board, X) == True or checkR(board, X) == True or checkC(board, X) == True or checkD2(board, X) == True:
        return X
    elif checkD(board, O) == True or checkR(board, O) == True or checkC(board, O) == True or checkD2(board, O) == True:
        return O
    else:
        return None

def tie(board):

    c = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] is not EMPTY:
                c+=1
    if c == 9 and winner(board) == None:
        return True

    return False

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if tie(board) == True or winner(board) is not None:
        return True
    else:
        return False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    elif tie(board) == True:
        return 0

def minv(board):

    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, maxv(result(board, action)))
    return v


def maxv(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, minv(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif player(board) == X:
        a = []
        for action in actions(board):
            a.append([minv(result(board, action)), action])

        return sorted(a, key = lambda x:x[0], reverse = True)[0][1]

    elif player(board) == O:
        a = []

        for action in actions(board):
            a.append([maxv(result(board, action)), action])

        return sorted(a, key = lambda x:x[0])[0][1]

