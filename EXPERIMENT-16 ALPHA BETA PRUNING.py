def alphabeta(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or is_terminal_state(node):
        return evaluate(node)
    if maximizing_player:
        value = -float('inf')
        for child in generate_children(node):
            value = max(value, alphabeta(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for child in generate_children(node):
            value = min(value, alphabeta(child, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value
def is_terminal_state(node):
def evaluate(node):
def generate_children(node):
def play_game():
    while not is_terminal_state(state):
        best_move = alphabeta(state, 2, -float('inf'), float('inf'), True)
        make_move(state, best_move)
        current_player = switch_player(current_player)
    print("The winner is:", current_player)
