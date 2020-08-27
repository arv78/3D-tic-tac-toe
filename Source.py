import numpy as np
import MiniMax
import is_goal
import Alpha_Beta_pruning
import heuristic
import heuristic_2
import Alpha_Beta_pruning_limited
import MiniMax_limited
import timeit


#printing the game board
def print_board(game_board):
    # the first batch
    for i in range(4):
        print("\n")
        for j in range(4):
            print(game_board[i][j], end = "  ")
            
    print("\n")
    # the second batch
    for i in range (4):
        print ("\n")
        for j in range (4,8):
            print(game_board[i][j], end = "  ")

    print("\n")

    
    # the third batch
    for i in range (4,8):
        print("\n")
        for j in range (4):
            print(game_board[i][j], end = "  ")
    print("\n")
    # the fourth batch
    for i in range (4,8):
        print("\n")
        for j in range (4,8):
            print(game_board[i][j], end = "  ") 
    print("\n")

    print("___________________")
    print("\n")

def main():
    # assembling the game board
    game_board = np.zeros((8,8), dtype = str)
    for i in range (8):
        for j in range(8):
            game_board[i][j] = "."
    selection = eval(input("1.computer vs computer\n2.computer vs random\n3.computer vs human\n"))
    if (selection == 1):
        flag = 0
        flag_2 = 0
        beginner = eval(input("who starts first?! \n1.computer1 \n2.computer2\n"))
        if (beginner == 2):
            flag = 1
        while (True):
            if (flag_2 == 0):
                print_board(game_board)
                flag_2 = 1
            if (flag == 0):
                # computer1's turn    
                # board = MiniMax.Minimax(game_board)
                start = timeit.default_timer()
                board = Alpha_Beta_pruning_limited.Minimax(game_board,"R")
                stop = timeit.default_timer()
                if (stop - start > 70):
                    print("B won! (60 sec passed!!)")
                    return
                print("computer1's move:")
                print('Time: ', stop - start)
                final_result = is_goal.is_goal(board)
                if (final_result != "D"):
                    print_board(board)
                    print(final_result," has won!!")
                    return 
                print_board(board)

            #computer2's turn
            flag = 0
            # board = MiniMax.Minimax(game_board)
            start = timeit.default_timer()
            board = Alpha_Beta_pruning_limited.Minimax(game_board,"B")
            stop = timeit.default_timer()
            if (stop - start > 70):
                    print("R won! (60 sec passed!!)")
                    return
            print("computer2's move:")
            print('Time: ', stop - start)
            final_result = is_goal.is_goal(board)
            if (final_result != "D"):
                print_board(board)
                print(final_result," has won!!")
                return 
            print_board(board)  

    elif (selection == 2):
        flag = 0
        flag_2 = 0
        beginner = eval(input("who starts first?! \n1.computer \n2.random\n"))
        if (beginner == 1):
            flag = 1
        while (True):
            if (flag_2 == 0):
                print_board(game_board)
                flag_2 = 1
            # random's turn
            if (flag == 0):
                start = timeit.default_timer()
                rand_x = np.random.randint(0,7)
                rand_y = np.random.randint(0,7)
                while(game_board[rand_x][rand_y] != "."):
                    rand_x = np.random.randint(0,7)
                    rand_y = np.random.randint(0,7)
                stop = timeit.default_timer()
                if (stop - start > 70):
                    print("B won! (60 sec passed!!)")
                    return
                print("computer's move:")
                print('Time: ', stop - start)
                game_board[rand_x][rand_y] = "R"
                final_result = is_goal.is_goal(game_board)
                if (final_result != "D"):
                    print_board(board)
                    print(final_result," has won!!")
                    return 
                print_board(board)

            flag = 0
            # board = MiniMax.Minimax(game_board)
            start = timeit.default_timer()
            board = Alpha_Beta_pruning_limited.Minimax(game_board,"B")
            stop = timeit.default_timer()
            if (stop - start > 70):
                print("R won! (60 sec passed!!)")
                return
            print("computer's move:")
            print('Time: ', stop - start)
            final_result = is_goal.is_goal(board)
            if (final_result != "D"):
                print_board(board)
                print(final_result," has won!!")
                return 
            print_board(board)
        
    elif (selection == 3):
        random_num = 0
        flag = 0
        flag_2 = 0
        beginner = eval(input("who starts first?! \n1.computer \n2.user\n"))
        if (beginner == 1):
            flag = 1
        
        while (True):
            if (flag_2 == 0):
                print_board(game_board)
                flag_2 = 1
            if (flag == 0):
                #run time calculation
                start = timeit.default_timer()
                user_matrix = eval(input("Matrix number: "))
                user_x,user_y = eval(input("Matrix index: "))
                stop = timeit.default_timer()
                if (stop - start > 70):
                    print("B won!! (60 sec passed)")
                    return
                print('Time: ', stop - start)

                user_y, user_x = user_y - 1, user_x - 1

                if (user_matrix == 3):
                    user_x = user_x + 4
                elif (user_matrix == 2):
                    user_y = user_y + 4
                elif (user_matrix == 4):
                    user_x = user_x + 4
                    user_y = user_y + 4

                if (game_board[user_x][user_y] == "."):
                    game_board[user_x][user_y] = "R"
                    print("\nUser's move:")
                    final_result = is_goal.is_goal(game_board)
                    if (final_result != "D"):
                        print_board(board)
                        print(final_result," has won!!")
                        return 
                    print_board(game_board)
                else:
                    print("Selected index is already used!")
                    return
            flag = 0
            # computer's turn
            if (random_num > 0):
                rand_x = np.random.randint(0,7)
                rand_y = np.random.randint(0,7)
                while(game_board[rand_x][rand_y] != "."):
                    rand_x = np.random.randint(0,7)
                    rand_y = np.random.randint(0,7)
                print("computer's move:")
                game_board[rand_x][rand_y] = "B"
                print_board(board)
                random_num -= 1
            else:
                start = timeit.default_timer()
                # board = MiniMax.Minimax(game_board)
                board = Alpha_Beta_pruning_limited.Minimax(game_board,"B")
                stop = timeit.default_timer()
                if (stop - start > 70):
                    print("R won! (60 sec passed!!)")
                    return
                print("computer's move:")
                print('Time: ', stop - start)
                final_result = is_goal.is_goal(board)
                if (final_result != "D"):
                    print_board(board)
                    print(final_result," has won!!")
                    return 
                print_board(board)

main()