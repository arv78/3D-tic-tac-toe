def is_goal(game_board):
    for i in range(len(game_board)):
        for j in range(len(game_board)):
            if (game_board[i][j] != "."):
                player = game_board[i][j]
                if (i == 0 or i == 4) :
                    if (game_board[i+1][j] == player and game_board[i+2][j] == player and game_board[i+3][j] == player):
                        return player
                if (j == 0 or j == 4) :
                    if (game_board[i][j+1] == player and game_board[i][j+2] == player and game_board[i][j+3] == player):
                        return player
                if ((i == 0 and j == 0) or (i == 0 and j == 4) or (i == 4 and j== 0) or (i == 4 and j == 4)):
                    if (game_board[i+1][j+1] == player and game_board[i+2][j+2] == player and game_board[i+3][j+3] == player):
                        return player
                if ((i == 0 and j == 3) or (i == 0 and j == 7) or (i == 4 and j==3) or (i == 4 and j == 7)):
                    if (game_board[i+1][j-1] == player and game_board[i+2][j-2] == player and game_board[i+3][j-3] == player):
                        return player
                if (i <= 3 and j <= 3):
                    if (game_board[i][j+4] == player and game_board[i+4][j] == player and game_board[i+4][j+4] == player):
                        return player
                    if (i == 0):
                        if (game_board[i+1][j+4] == player and game_board[i+6][j] == player and game_board[i+7][j+4] == player):
                            return player
                        if (j == 0):
                            if (game_board[i+1][j+5] == player and game_board[i+6][j+2] == player and game_board[i+7][j+7] == player):
                                return player
                        if (j == 3):
                            if (game_board[i+1][j+3] == player and game_board[i+6][j-2] == player and game_board[i+7][j+1] == player):
                                return player
                    if (i == 3):
                        if (game_board[i-1][j+4] == player and game_board[i+2][j] == player and game_board[i+1][j+4] == player):
                            return player
                        if (j == 0):
                            if (game_board[i-1][j+5] == player and game_board[i+2][j+2] == player and game_board[i+1][j+7] == player):
                                return player
                        if (j == 3):
                            if (game_board[i-1][j+3] == player and game_board[i+2][j-2] == player and game_board[i+1][j+1] == player):
                                return player
                    if (j == 0):
                        if (game_board[i][j+5] == player and game_board[i+4][j+2] == player and game_board[i+4][j+7] == player):
                            return player
                    if (j == 3):
                        if (game_board[i][j+3] == player and game_board[i+4][j-2] == player and game_board[i+4][j+1] == player):
                            return player
    if ("." in game_board):
        return "D"
    else:
        return "F"                    