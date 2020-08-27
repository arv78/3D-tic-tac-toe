import numpy as np

def test_heu():
    game_board = np.zeros((8,8), dtype = str)
    for i in range (8):
        for j in range(8):
            game_board[i][j] = "."

    game_board[0][0] = "B"
    game_board[0][1] = "B"
    game_board[0][2] = "R"
    # game_board[0][1] = "B"
    # game_board[1][1] = "B"
    # game_board[2][1] = "B"
    # game_board[0][0] = "B"
    points=heuristic(game_board)
    print(points)


def heuristic(game_board):
    best_point = 0
    best_player = ""
    for i in range (len(game_board)):
        for j in range (len(game_board)):
            if (game_board[i][j] != "."):
                player = game_board[i][j]
                if (i == 0 or i == 4):
                    if (game_board[i+1][j] == player):
                        point = 0
                        if (player == "R"):
                            point = 1
                            point += 1
                        elif (player == "B"):
                            point += 1
                        if (point >= best_point):
                            best_point = point
                            best_player = player
                        if (game_board[i+2][j] == player):
                            if (player == "R"):
                                point += 1
                            elif (player == "B"):
                                point += 1
                            if (point >= best_point):
                                best_point = point
                                best_player = player
                if (i == 1 or i == 5):
                    if (game_board[i+1][j] == player):
                        point = 0
                        if (player == "R"):
                            point = 1
                            point += 1
                        elif (player == "B"):
                            point += 1
                        if (point >= best_point):
                            best_point = point
                            best_player = player
                        if (game_board[i+2][j] == player):
                            if (player == "R"):
                                point += 1
                            elif (player == "B"):
                                point += 1
                            if (point >= best_point):
                                best_point = point
                                best_player = player
                if (i == 2 or i == 6):
                    if (game_board[i+1][j] == player):
                        point = 0
                        if (player == "R"):
                            point = 1
                            point += 1
                        elif (player == "B"):
                            point += 1
                        if (point >= best_point):
                            best_point = point
                            best_player = player
                if (j == 0 or j == 4):
                    if (game_board[i][j+1] == player):
                        point = 0
                        if (player == "R"):
                            point = 1
                            point += 1
                        elif (player == "B"):
                            point += 1
                        if (point >= best_point):
                            best_point = point
                            best_player = player
                        if (game_board[i][j+2] == player):
                            if (player == "R"):
                                point += 1
                            elif (player == "B"):
                                point += 1
                            if (point >= best_point):
                                best_point = point
                                best_player = player
                if (j == 1 or j == 5):
                    if (game_board[i][j+1] == player):
                        point = 0
                        if (player == "R"):
                            point = 1
                            point += 1
                        elif (player == "B"):
                            point += 1
                        if (point >= best_point):
                            best_point = point
                            best_player = player
                        if (game_board[i][j+2] == player):
                            if (player == "R"):
                                point += 1
                            elif (player == "B"):
                                point += 1
                            if (point >= best_point):
                                best_point = point
                                best_player = player
                if (j == 2 or j == 6):
                    if (game_board[i][j+1] == player):
                        point = 0
                        if (player == "R"):
                            point = 1
                            point += 1
                        elif (player == "B"):
                            point += 1
                        if (point >= best_point):
                            best_point = point
                            best_player = player
                if ((i == 0 and j == 0) or (i == 0 and j == 4) or (i == 4 and j== 0) or (i == 4 and j == 4)):
                    if (game_board[i+1][j+1] == player):
                        point = 0
                        if (player == "R"):
                            point = 1
                            point += 1
                        elif (player == "B"):
                            point += 1
                        if (point >= best_point):
                            best_point = point
                            best_player = player
                        if (game_board[i+2][j+2] == player):
                            if (player == "R"):
                                point += 1
                            elif (player == "B"):
                                point += 1
                            if (point >= best_point):
                                best_point = point
                                best_player = player
                if ((i == 1 and j == 1) or (i == 1 and j == 5) or (i == 5 and j== 1) or (i == 5 and j == 5)):
                    if (game_board[i+1][j+1] == player):
                        point = 0
                        if (player == "R"):
                            point = 1
                            point += 1
                        elif (player == "B"):
                            point += 1
                        if (point >= best_point):
                            best_point = point
                            best_player = player
                        if (game_board[i+2][j+2] == player):
                            if (player == "R"):
                                point += 1
                            elif (player == "B"):
                                point += 1
                            if (point >= best_point):
                                best_point = point
                                best_player = player
                if ((i == 2 and j == 2) or (i == 2 and j == 6) or (i == 6 and j== 2) or (i == 6 and j == 6)):
                    if (game_board[i+1][j+1] == player):
                        point = 0
                        if (player == "R"):
                            point = 1
                            point += 1
                        elif (player == "B"):
                            point += 1
                        if (point >= best_point):
                            best_point = point
                            best_player = player
                if ((i == 0 and j == 3) or (i == 0 and j == 7) or (i == 4 and j==3) or (i == 4 and j == 7)):
                    if (game_board[i+1][j-1] == player):
                        point = 0
                        if (player == "R"):
                            point = 1
                            point += 1
                        elif (player == "B"):
                            point += 1
                        if (point >= best_point):
                            best_point = point
                            best_player = player
                        if (game_board[i+2][j-2] == player):
                            if (player == "R"):
                                point += 1
                            elif (player == "B"):
                                point += 1
                            if (point >= best_point):
                                best_point = point
                                best_player = player
                if ((i == 1 and j == 2) or (i == 1 and j == 6) or (i == 5 and j==2) or (i == 5 and j == 6)):
                    if (game_board[i+1][j-1] == player):
                        point = 0
                        if (player == "R"):
                            point = 1
                            point += 1
                        elif (player == "B"):
                            point += 1
                        if (point >= best_point):
                            best_point = point
                            best_player = player
                        if (game_board[i+2][j-2] == player):
                            if (player == "R"):
                                point += 1
                            elif (player == "B"):
                                point += 1
                            if (point >= best_point):
                                best_point = point
                                best_player = player
                if ((i == 2 and j == 1) or (i == 2 and j == 5) or (i == 6 and j==1) or (i == 6 and j == 5)):
                    if (game_board[i+1][j-1] == player):
                        point = 0
                        if (player == "R"):
                            point = 1
                            point += 1
                        elif (player == "B"):
                            point += 1
                        if (point >= best_point):
                            best_point = point
                            best_player = player
                if (i <= 3 and j <= 3):
                    if (game_board[i][j+4] == player):
                        point = 0
                        if (player == "R"):
                            point = 1
                            point += 1
                        elif (player == "B"):
                            point += 1
                        if (point >= best_point):
                            best_point = point
                            best_player = player
                        if (game_board[i+4][j] == player):
                            if (player == "R"):
                                point += 1
                            elif (player == "B"):
                                point += 1
                            if (point >= best_point):
                                best_point = point
                                best_player = player
                    if (i == 0):
                        if (game_board[i+1][j+4] == player):
                            point = 0
                            if (player == "R"):
                                point = 1
                                point += 1
                            elif (player == "B"):
                                point += 1
                            if (point >= best_point):
                                best_point = point
                                best_player = player
                            if(game_board[i+6][j] == player):
                                if (player == "R"):
                                    point = 1
                                    point += 1
                                elif (player == "B"):
                                    point += 1
                                if (point >= best_point):
                                    best_point = point
                                    best_player = player
                        if (j == 0):
                            if (game_board[i+1][j+5] == player):
                                point = 0
                                if (player == "R"):
                                    point = 1
                                    point += 1
                                elif (player == "B"):
                                    point += 1
                                if (point >= best_point):
                                    best_point = point
                                    best_player = player
                                if (game_board[i+6][j+2] == player):
                                    if (player == "R"):
                                        point = 1
                                        point += 1
                                    elif (player == "B"):
                                        point += 1
                                    if (point >= best_point):
                                        best_point = point
                                        best_player = player
                        if (j == 3):
                            if (game_board[i+1][j+3] == player):
                                point = 0
                                if (player == "R"):
                                    point = 1
                                    point += 1
                                elif (player == "B"):
                                    point += 1
                                if (point >= best_point):
                                    best_point = point
                                    best_player = player
                                if (game_board[i+6][j-2] == player):
                                    if (player == "R"):
                                        point = 1
                                        point += 1
                                    elif (player == "B"):
                                        point += 1
                                    if (point >= best_point):
                                        best_point = point
                                        best_player = player
                    if (i == 3):
                        if (game_board[i-1][j+4] == player):
                            point = 0
                            if (player == "R"):
                                point = 1
                                point += 1
                            elif (player == "B"):
                                point += 1
                            if (point >= best_point):
                                best_point = point
                                best_player = player
                            if (game_board[i+2][j] == player):
                                if (player == "R"):
                                    point = 1
                                    point += 1
                                elif (player == "B"):
                                    point += 1
                                if (point >= best_point):
                                    best_point = point
                                    best_player = player
                        if (j == 0):
                            if (game_board[i-1][j+5] == player):
                                point = 0
                                if (player == "R"):
                                    point = 1
                                    point += 1
                                elif (player == "B"):
                                    point += 1
                                if (point >= best_point):
                                    best_point = point
                                    best_player = player
                                if (game_board[i+2][j+2] == player):
                                    if (player == "R"):
                                        point = 1
                                        point += 1
                                    elif (player == "B"):
                                        point += 1
                                    if (point >= best_point):
                                        best_point = point
                                        best_player = player
                        if (j == 3):
                            if (game_board[i-1][j+3] == player):
                                point = 0
                                if (player == "R"):
                                    point = 1
                                    point += 1
                                elif (player == "B"):
                                    point += 1
                                if (point >= best_point):
                                    best_point = point
                                    best_player = player
                                if (game_board[i+2][j-2] == player):
                                    if (player == "R"):
                                        point = 1
                                        point += 1
                                    elif (player == "B"):
                                        point += 1
                                    if (point >= best_point):
                                        best_point = point
                                        best_player = player
                    if (j == 0):
                        if (game_board[i][j+5] == player):
                            point = 0
                            if (player == "R"):
                                point = 1
                                point += 1
                            elif (player == "B"):
                                point += 1
                            if (point >= best_point):
                                best_point = point
                                best_player = player
                            if (game_board[i+4][j+2] == player):
                                if (player == "R"):
                                    point = 1
                                    point += 1
                                elif (player == "B"):
                                    point += 1
                                if (point >= best_point):
                                    best_point = point
                                    best_player = player
                    if (j == 3):
                        if (game_board[i][j+3] == player):
                            point = 0
                            if (player == "R"):
                                point = 1
                                point += 1
                            elif (player == "B"):
                                point += 1
                            if (point >= best_point):
                                best_point = point
                                best_player = player
                            if (game_board[i+4][j-2] == player):
                                if (player == "R"):
                                    point = 1
                                    point += 1
                                elif (player == "B"):
                                    point += 1
                                if (point >= best_point):
                                    best_point = point
                                    best_player = player
                if (i <= 3  and (j > 3 and j <= 7)):
                    if (game_board[i+4][j-4] == player):
                        point = 0
                        if (player == "R"):
                            point = 1
                            point += 1
                        elif (player == "B"):
                            point += 1
                        if (point >= best_point):
                            best_point = point
                            best_player = player
                        if (game_board[i+4][j] == player):
                            if (player == "R"):
                                point += 1
                            elif (player == "B"):
                                point += 1
                            if (point >= best_point):
                                best_point = point
                                best_player = player
                    if (i == 1):
                        if (game_board[i+5][j-4] == player):
                            point = 0
                            if (player == "R"):
                                point = 1
                                point += 1
                            elif (player == "B"):
                                point += 1
                            if (point >= best_point):
                                best_point = point
                                best_player = player
                            if(game_board[i+6][j] == player):
                                if (player == "R"):
                                    point = 1
                                    point += 1
                                elif (player == "B"):
                                    point += 1
                                if (point >= best_point):
                                    best_point = point
                                    best_player = player
                        if (j == 5):
                            if (game_board[i+5][j-3] == player):
                                point = 0
                                if (player == "R"):
                                    point = 1
                                    point += 1
                                elif (player == "B"):
                                    point += 1
                                if (point >= best_point):
                                    best_point = point
                                    best_player = player
                                if (game_board[i+6][j+2] == player):
                                    if (player == "R"):
                                        point = 1
                                        point += 1
                                    elif (player == "B"):
                                        point += 1
                                    if (point >= best_point):
                                        best_point = point
                                        best_player = player
                        if (j == 6):
                            if (game_board[i+5][j-5] == player):
                                point = 0
                                if (player == "R"):
                                    point = 1
                                    point += 1
                                elif (player == "B"):
                                    point += 1
                                if (point >= best_point):
                                    best_point = point
                                    best_player = player
                                if (game_board[i+6][j-2] == player):
                                    if (player == "R"):
                                        point = 1
                                        point += 1
                                    elif (player == "B"):
                                        point += 1
                                    if (point >= best_point):
                                        best_point = point
                                        best_player = player   
                    if (i == 2):
                        if (game_board[i+3][j-4] == player):
                            point = 0
                            if (player == "R"):
                                point = 1
                                point += 1
                            elif (player == "B"):
                                point += 1
                            if (point >= best_point):
                                best_point = point
                                best_player = player
                            if (game_board[i+2][j] == player):
                                if (player == "R"):
                                    point = 1
                                    point += 1
                                elif (player == "B"):
                                    point += 1
                                if (point >= best_point):
                                    best_point = point
                                    best_player = player
                        if (j == 5):
                            if (game_board[i+3][j-3] == player):
                                point = 0
                                if (player == "R"):
                                    point = 1
                                    point += 1
                                elif (player == "B"):
                                    point += 1
                                if (point >= best_point):
                                    best_point = point
                                    best_player = player
                                if (game_board[i+2][j+2] == player):
                                    if (player == "R"):
                                        point = 1
                                        point += 1
                                    elif (player == "B"):
                                        point += 1
                                    if (point >= best_point):
                                        best_point = point
                                        best_player = player
                        if (j == 6):
                            if (game_board[i+3][j-5] == player):
                                point = 0
                                if (player == "R"):
                                    point = 1
                                    point += 1
                                elif (player == "B"):
                                    point += 1
                                if (point >= best_point):
                                    best_point = point
                                    best_player = player
                                if (game_board[i+2][j-2] == player):
                                    if (player == "R"):
                                        point = 1
                                        point += 1
                                    elif (player == "B"):
                                        point += 1
                                    if (point >= best_point):
                                        best_point = point
                                        best_player = player
                    if (j == 5):
                        if (game_board[i+4][j-3] == player):
                            point = 0
                            if (player == "R"):
                                point = 1
                                point += 1
                            elif (player == "B"):
                                point += 1
                            if (point >= best_point):
                                best_point = point
                                best_player = player
                            if (game_board[i+4][j+2] == player):
                                if (player == "R"):
                                    point = 1
                                    point += 1
                                elif (player == "B"):
                                    point += 1
                                if (point >= best_point):
                                    best_point = point
                                    best_player = player
                    if (j == 6):
                        if (game_board[i+4][j-5] == player):
                            point = 0
                            if (player == "R"):
                                point = 1
                                point += 1
                            elif (player == "B"):
                                point += 1
                            if (point >= best_point):
                                best_point = point
                                best_player = player
                            if (game_board[i+4][j-2] == player):
                                if (player == "R"):
                                    point = 1
                                    point += 1
                                elif (player == "B"):
                                    point += 1
                                if (point >= best_point):
                                    best_point = point
                                    best_player = player                     
                if (j <= 3  and (i > 3 and i <= 7)):
                    if (game_board[i][j+4] == player):
                        point = 0
                        if (player == "R"):
                            point = 1
                            point += 1
                        elif (player == "B"):
                            point += 1
                        if (point >= best_point):
                            best_point = point
                            best_player = player
                    if (i == 6):
                        if (game_board[i+1][j+4] == player):
                            point = 0
                            if (player == "R"):
                                point = 1
                                point += 1
                            elif (player == "B"):
                                point += 1
                            if (point >= best_point):
                                best_point = point
                                best_player = player
                        if (j == 2):
                            if (game_board[i+1][j+5] == player):
                                point = 0
                                if (player == "R"):
                                    point = 1
                                    point += 1
                                elif (player == "B"):
                                    point += 1
                                if (point >= best_point):
                                    best_point = point
                                    best_player = player 
                        if (j == 1):
                            if (game_board[i+1][j+3] == player):
                                point = 0
                                if (player == "R"):
                                    point = 1
                                    point += 1
                                elif (player == "B"):
                                    point += 1
                                if (point >= best_point):
                                    best_point = point
                                    best_player = player
                    if (i == 5):
                        if (game_board[i-1][j+4] == player):
                            point = 0
                            if (player == "R"):
                                point = 1
                                point += 1
                            elif (player == "B"):
                                point += 1
                            if (point >= best_point):
                                best_point = point
                                best_player = player
                        if (j == 2):
                            if (game_board[i-1][j+5] == player):
                                point = 0
                                if (player == "R"):
                                    point = 1
                                    point += 1
                                elif (player == "B"):
                                    point += 1
                                if (point >= best_point):
                                    best_point = point
                                    best_player = player
                        if (j == 1):
                            if (game_board[i-1][j+3] == player):
                                point = 0
                                if (player == "R"):
                                    point = 1
                                    point += 1
                                elif (player == "B"):
                                    point += 1
                                if (point >= best_point):
                                    best_point = point
                                    best_player = player
                    if (j == 2):
                        if (game_board[i][j+5] == player):
                            point = 0
                            if (player == "R"):
                                point = 1
                                point += 1
                            elif (player == "B"):
                                point += 1
                            if (point >= best_point):
                                best_point = point
                                best_player = player
                    if (j == 1):
                        if (game_board[i][j+3] == player):
                            point = 0
                            if (player == "R"):
                                point = 1
                                point += 1
                            elif (player == "B"):
                                point += 1
                            if (point >= best_point):
                                best_point = point
                                best_player = player
    return best_player,best_point            