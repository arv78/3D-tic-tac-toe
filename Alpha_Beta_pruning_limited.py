import is_goal
import numpy as np
import heuristic_2
import heuristic


def copy_matrix(game_board):
    new_board = np.zeros((8,8), dtype = str)
    for i in range (len(game_board)):
        for j in range (len(game_board)):
            new_board[i][j] = game_board[i][j]
    return new_board  

def Minimax(game_board,turn):
    pos_inf = 10000
    neg_inf = -10000
    v,best_x,best_y = Max_value(game_board,neg_inf,pos_inf,3,-1,-1,turn)
    print("final_best x:",best_x," final_best y:",best_y)
    if (best_x != -1 and best_y != -1):
        game_board[best_x][best_y] = turn
    return game_board

def Max_value(game_board,alpha,beta,level,best_x,best_y,turn):
    #print("max")
    result = is_goal.is_goal(game_board)
    if (result != "D"):
        if (turn == "B"):
            if (result == "R"):
                return -100, best_x, best_y
            if (result == "B"):
                return 100, best_x, best_y
            if (result == "F"):
                return 0, best_x, best_y
        elif (turn == "R"):
            if (result == "R"):
                return 100, best_x, best_y
            if (result == "B"):
                return -100, best_x, best_y
            if (result == "F"):
                return 0, best_x, best_y
    
    if(level <= 0):
        score = heuristic_2.heuristic(game_board,turn)
        # if(color=="R"):
        #     score= (-1)*score
        return score,best_x,best_y
    v = -10000
    Actions = []
    for i in range (len(game_board)):
        for j in range(len(game_board)):
            if (game_board[i][j] == "."):
                Actions.append([i,j])

    for i in range (len(Actions)):
        x,y = Actions[i]

        new_board = copy_matrix(game_board)
        if (turn == "B"):
            new_board[x][y] = "B"
        elif (turn == "R"):
            new_board[x][y] = "R"
        L,best_x,best_y = Min_value(new_board,alpha,beta,level-1,best_x,best_y,turn)
        L = max(v,L)
        # print("V:" ,v)
        # print("L:",L)
        # input("inter:")
        if (L > v):
            if (level == 3):
                best_x = x
                best_y = y
                print("best x:",best_x," best y:",best_y)
            #     print("best x:",best_x," best y:",best_y)
            v = L

        if (v >= beta):
            return v,best_x,best_y
        alpha = max(v,alpha)
    return v,best_x,best_y


def Min_value(game_board,alpha,beta,level,best_x,best_y,turn):
    #print("min")
    result = is_goal.is_goal(game_board)
    if (result != "D"):
        if (turn == "B"):
            if (result == "R"):
                return -100, best_x, best_y
            if (result == "B"):
                return 100, best_x, best_y
            if (result == "F"):
                return 0, best_x, best_y
        elif (turn == "R"):
            if (result == "R"):
                return 100, best_x, best_y
            if (result == "B"):
                return -100, best_x, best_y
            if (result == "F"):
                return 0, best_x, best_y

    if(level <= 0):
        score = heuristic_2.heuristic(game_board,turn)
        # if(color=="R"):
        #     score= (-1)*score
        # print("min_score: ",score)
        return score,best_x,best_y
    v = 10000
    Actions = []
    for i in range (len(game_board)):
        for j in range(len(game_board)):
            if (game_board[i][j] == "."):
                Actions.append([i,j])

    for i in range (len(Actions)):
        x,y = Actions[i]
        new_board = copy_matrix(game_board)
        if (turn == "B"):
            new_board[x][y] = "R"
        elif (turn == "R"):
            new_board[x][y] = "B"
        L,best_x,best_y = Max_value(new_board,alpha,beta,level-1,best_x,best_y,turn)
        v = min(v,L)
        if (v <= alpha):
            return v,best_x,best_y
        beta = min (v , beta)
    return v,best_x,best_y
 