import copy
def minimax(board, player, depth, alpha, beta):
    if is_terminal_state(board):
        return evaluate(board, player)
    if player == 'X':
        best_value = -float('inf')
        for move in get_valid_moves(board):
            new_board = copy.deepcopy(board)
            make_move(new_board, move)
            value = minimax(new_board, 'O', depth + 1, alpha, beta)
            best_value = max(best_value, value)
            alpha = max(alpha, best_value)
            if alpha >= beta:
                break
    else:
        best_value = float('inf')
        for move in get_valid_moves(board):
            new_board = copy.deepcopy(board)
            make_move(new_board, move)
            value = minimax(new_board, 'X', depth + 1, alpha, beta)
            best_value = min(best_value, value)
            beta = min(beta, best_value)
            if alpha >= beta:
                break
    if depth == 0:
        return best_value, move
    return best_value
def is_terminal_state(board):
    if any(all(cell == player for cell in row) for row in board):
        return True
    if any(all(board[row][col] == player for row in range(3)) for col in range(3)):
        return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    if all(cell != '-' for row in board for cell in row):
        return True

    return False

def evaluate(board, player):
    if is_terminal_state(board) and check_winner(board, player):
        return 10
    elif is_terminal_state(board) and not check_winner(board, player):
        return -10
    else:
        return 0
def get_valid_moves(board):
    valid_moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == '-':
                valid_moves.append((row, col))
    return valid_moves
def make_move(board, move):
    row, col = move
    board[row][col] = 'X'
def check_winner(board, player):
    if any(all(cell == player for cell in row) for row in board):
        return True
    if any(all(board[row][col] == player for row in range(3)) for col in range(3)):
        return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
def play_game():
    board = [['-', '-', '-'],
             ['-', '-', '-'],
             ['-', '-', '-']]
    current_player = 'X'
    while True:
        display_board(board)
        print("Player", current_player, "turn.")
        if current_player == 'X':
            best_value, move = minimax(board, current_player, 2, -float('inf'), float('inf'))
            make_move(board, move)
        else:
            move = get_user_move(board)
            make_move(board, move)
        if check_winner(board, current_player):
            display_board(board)
            print("Player", current_player, "wins!")
            break
        current_player = switch_player(current_player)
    print("Game over.")
def display_board(board):
    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()
def get_user_move(board):
    while True:
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))
