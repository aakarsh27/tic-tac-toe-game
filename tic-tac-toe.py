import random

def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def take_turn(player, board):
    print(player + "'s turn.")
    if player == "X":  # Human player
        position = input("Choose a position from 1-9: ")
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] or board[int(position) - 1] != "-":
            position = input("Invalid input. Choose a position from 1-9: ")
        position = int(position) - 1
    else:  # AI player
        position = get_ai_move(board)
    board[position] = player
    print_board(board)

def check_game_over(board):
    if (board[0] == board[1] == board[2] != "-") or \
       (board[3] == board[4] == board[5] != "-") or \
       (board[6] == board[7] == board[8] != "-") or \
       (board[0] == board[3] == board[6] != "-") or \
       (board[1] == board[4] == board[7] != "-") or \
       (board[2] == board[5] == board[8] != "-") or \
       (board[0] == board[4] == board[8] != "-") or \
       (board[2] == board[4] == board[6] != "-"):
        return "win"
    elif "-" not in board:
        return "tie"
    else:
        return "play"

def play_game():
    board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    print_board(board)
    current_player = "X"
    game_over = False
    while not game_over:
        take_turn(current_player, board)
        game_result = check_game_over(board)
        if game_result == "win":
            print(current_player + " wins!")
            game_over = True
        elif game_result == "tie":
            print("It's a tie!")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"

def get_ai_move(board):
    # Get all available moves
    available_moves = [i for i in range(len(board)) if board[i] == "-"]
    # Simulate each available move and get the score
    best_score = float("-inf")
    best_move = None
    for move in available_moves:
        board[move] = "O"  # Assuming AI is O
        score = minimax(board, False)
        board[move] = "-"  # Undo the move
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def minimax(board, is_maximizing):
    # Check if the game is over
    result = check_game_over(board)
    if result == "win":
        return 1 if is_maximizing else -1
    elif result == "tie":
        return 0
    # Maximizing player (AI)
    if is_maximizing:
        best_score = float("-inf")
        for i in range(len(board)):
            if board[i] == "-":
                board[i] = "O"  # Assuming AI is O
                score = minimax(board, False)
                board[i] = "-"  # Undo the move
                best_score = max(score, best_score)
        return best_score
    # Minimizing player (Human)
    else:
        best_score = float("inf")
        for i in range(len(board)):
            if board[i] == "-":
                board[i] = "X"  # Assuming Human is X
                score = minimax(board, True)
                board[i] = "-"  # Undo the move
                best_score = min(score, best_score)
        return best_score

play_game()
