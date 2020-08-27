import is_goal
import numpy as np
import heuristic_2
import heuristic

best_x = -1
best_y = -1

def copy_matrix(game_board):
    new_board = np.zeros((8,8), dtype = str)
    for i in range (len(game_board)):
        for j in range (len(game_board)):
            new_board[i][j] = game_board[i][j]
    return new_board

def Minimax(game_board):
    Max_value(game_board,3)
    if (best_x != -1 and best_y != -1):
        game_board[best_x][best_y] = "B"
    return game_board

def Max_value(game_board,level):
    #print("max\n")
    result = is_goal.is_goal(game_board)
    #print("continue\n")
    if (result != "D"):
        if (result == "R"):
            return -100
        if (result == "B"):
            return 100
        if (result == "F"):
            return 0
    
    if(level <= 0):
        score = heuristic_2.heuristic(game_board,"B")
        # if(color=="R"):
        #     score= (-1)*score
        return score
    v = -10000
    Actions = []
    # successor
    for i in range (len(game_board)):
        for j in range(len(game_board)):
            if (game_board[i][j] == "."):
                Actions.append([i,j])

    for i in range (len(Actions)):
        x,y = Actions[i]
        new_board = copy_matrix(game_board)
        new_board[x][y] = "B"
        MV = Min_value(new_board,level-1)
        if (MV > v):
            if (level ==3 ):
                global best_x
                global best_y
                best_x = x
                best_y = y
            v = MV
    return v


def Min_value(game_board,level):
    #print("min\n")
    result = is_goal.is_goal(game_board)
    if (result != "D"):
        if (result == "R"):
            return -100
        if (result == "B"):
            return 100
        if (result == "F"):
            return 0

    if(level <= 0):
        score = heuristic_2.heuristic(game_board,"B")
        # if(color=="R"):
        #     score= (-1)*score
        
        #print("min score",score)
        return score

    v = 10000
    Actions = []
    for i in range (len(game_board)):
        for j in range(len(game_board)):
            if (game_board[i][j] == "."):
                Actions.append([i,j])

    for i in range (len(Actions)):
        x,y = Actions[i]
        new_board = copy_matrix(game_board)
        new_board[x][y] = "R"
        v = min(v,Max_value(new_board,level-1))
    return v
 