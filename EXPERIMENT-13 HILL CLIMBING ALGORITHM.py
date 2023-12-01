import numpy as np
def hill_climbing(landscape, max_iterations):
    current_state = np.random.randint(0, landscape.shape[0])
    current_score = landscape[current_state]
    best_state = current_state
    best_score = current_score
    for _ in range(max_iterations):
        neighbours = [
            (i, landscape[i]) for i in range(current_state)
            if i != current_state
        ]
        best_neighbour, best_neighbour_score = max(neighbours, key=lambda x: x[1])
        if best_neighbour_score > current_score:
            current_state = best_neighbour
            current_score = best_neighbour_score
        else:
            break
        if current_score > best_score:
            best_state = current_state
            best_score = current_score
    return best_state, best_score
landscape = np.array([1, 2, 3, 4, 5])
max_iterations = 100
best_state, best_score = hill_climbing(landscape, max_iterations)
print("Best state:", best_state)
print("Best score:", best_score)
