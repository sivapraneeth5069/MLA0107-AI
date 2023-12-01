def is_valid_state(state):
    for side in state:
        if side.count('M') < side.count('C') and side.count('M') > 0:
            return False
    return True
def is_goal_state(state):
    return state[1] == ['M', 'M', 'M', 'C', 'C', 'C']
def generate_next_states(state):
    next_states = []
    for i in range(1, 3):  
        for j in range(2):
            for k in range(2):
                new_state = [list(state[0]), list(state[1])]
                if j == 0:
                    new_state[0].remove('M')
                    new_state[1].append('M')
                else:
                    new_state[0].remove('C')
                    new_state[1].append('C')
                if k == 0:
                    new_state[0].remove('M')
                    new_state[1].append('M')
                else:
                    new_state[0].remove('C')
                    new_state[1].append('C')
                if is_valid_state(new_state):
                    next_states.append(new_state)
    return next_states
def print_state(state):
    print("Left side:", state[0])
    print("Right side:", state[1])
    print()
def solve_puzzle():
    initial_state = [['M', 'M', 'M', 'C', 'C', 'C'], []]
    frontier = [initial_state]
    visited = set()
    while frontier:
        current_state = frontier.pop(0)
        if is_goal_state(current_state):
            print("Solution found:")
            for step, state in enumerate(visited):
                print("Step", step + 1)
                print_state(state)
            print("Step", len(visited) + 1)
            print_state(current_state)
            return
        visited.add(tuple(current_state[0] + ['B'] + current_state[1]))
        next_states = generate_next_states(current_state)
        for next_state in next_states:
            if tuple(next_state[0] + ['B'] + next_state[1]) not in visited:
                frontier.append(next_state)
    print("No solution found.")
solve_puzzle()
