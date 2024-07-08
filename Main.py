# tic_tac_toe.py

import random

def print_board(board):
    print("---------")
    for row in board:
        print("| " + " | ".join(row) + " |")
    print("---------")

def check_winner(board, player):
    # Check rows, columns, and diagonals
    win_conditions = (
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    )
    return [player, player, player] in win_conditions

def get_user_move(board, current_player):
    while True:
        try:
            row = int(input(f"Player {current_player}, enter the row (1-3): ")) - 1
            col = int(input(f"Player {current_player}, enter the column (1-3): ")) - 1
            if board[row][col] == " ":
                board[row][col] = current_player
                break
            else:
                print("This cell is already taken. Choose another one.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 3.")

def get_computer_move(board, current_player):
    print(f"Computer's turn ({current_player}):")
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            board[row][col] = current_player
            break

def tic_tac_toe():
    print("Welcome to Tic Tac Toe!")
    print("Choose an option:")
    print("1. Play against another player")
    print("2. Play against the computer")
    choice = input("Enter your choice (1 or 2): ")
    
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        
        if choice == "1":
            if current_player == "X":
                get_user_move(board, current_player)
            else:
                get_user_move(board, current_player)
        elif choice == "2":
            if current_player == "X":
                get_user_move(board, current_player)
            else:
                get_computer_move(board, current_player)
        else:
            print("Invalid choice. Please enter 1 or 2.")
            continue
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif all(board[i][j] != " " for i in range(3) for j in range(3)):
            print_board(board)
            print("It's a tie!")
            break
        
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
