import is_goal
import numpy as np

best_x = -1
best_y = -1

def copy_matrix(game_board):
    new_board = np.zeros((8,8), dtype = str)
    for i in range (len(game_board)):
        for j in range (len(game_board)):
            new_board[i][j] = game_board[i][j]
    return new_board

def Minimax(game_board):
    v = Max_value(game_board)
    if (best_x != -1 and best_y != -1):
        game_board[best_x][best_y] = "B"
    return game_board

def Max_value(game_board):
    result = is_goal.is_goal(game_board)
    if (result != "D"):
        if (result == "R"):
            return -1
        if (result == "B"):
            return 1
        if (result == "F"):
            return 0
    v = -10000
    Actions = []
    # successor
    for i in range (len(game_board)):
        for j in range(len(game_board)):
            if (game_board[i][j] == "."):
                Actions.append(i)
                Actions.append(j)

    for i in range (len(Actions)//2):
        y = Actions.pop()
        x = Actions.pop()
        new_board = copy_matrix(game_board)
        new_board[x][y] = "B"
        MV = Min_value(new_board)
        if (MV > v):
            best_x = x
            best_y = y
            v = MV
    return v


def Min_value(game_board):
    result = is_goal.is_goal(game_board)
    if (result != "D"):
        if (result == "R"):
            return -1
        if (result == "B"):
            return 1
        if (result == "F"):
            return 0
    v = 10000
    Actions = []
    for i in range (len(game_board)):
        for j in range(len(game_board)):
            if (game_board[i][j] == "."):
                Actions.append(i)
                Actions.append(j)

    for i in range (len(Actions)//2):
        y = Actions.pop()
        x = Actions.pop()
        new_board = copy_matrix(game_board)
        new_board[x][y] = "R"
        v = min(v,Max_value(new_board))
    return v
 