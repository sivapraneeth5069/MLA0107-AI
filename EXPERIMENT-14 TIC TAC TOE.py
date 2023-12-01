def display_board(board):
    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()
def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
def make_move(board, player, row, col):
    if board[row][col] != '-':
        return False
    board[row][col] = player
    return True
def switch_player(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'
def play_game():
    board = [['-', '-', '-'],
             ['-', '-', '-'],
             ['-', '-', '-']]
    current_player = 'X'
    while True:
        display_board(board)
        print("Player", current_player, "turn.")
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))
        if not make_move(board, current_player, row, col):
            print("Invalid move. Please try again.")
            continue
        if check_winner(board, current_player):
            display_board(board)
            print("Player", current_player, "wins!")
            break
        current_player = switch_player(current_player)
    print("Game over.")
if __name__ == "__main__":
    play_game()
