import random
import numpy as np

def simulated_annealing(objective, bounds, n_iterations, step_size, init_temp, cooling_rate):
    current_point = generate_point(bounds)
    current_value = objective(current_point)
    best_point = current_point
    best_value = current_value
    for i in range(n_iterations):
        neighbor = generate_neighbor(current_point, step_size, bounds)
        neighbor_value = objective(neighbor)
        delta_energy = neighbor_value - current_value
        if delta_energy <= 0:
            p_accept = 1
        else:
            p_accept = np.exp(-delta_energy / init_temp)
        if random.random() < p_accept:
            current_point = neighbor
            current_value = neighbor_value
        if current_value < best_value:
            best_point = current_point
            best_value = current_value
        init_temp *= cooling_rate
    return best_point, best_value
def generate_point(bounds):
    point = []
    for bound in bounds:
        lower_bound, upper_bound = bound
        point.append(random.uniform(lower_bound, upper_bound))
    return point
def generate_neighbor(current_point, step_size, bounds):
    neighbor = []
    for i, bound in enumerate(bounds):
        lower_bound, upper_bound = bound
        perturbation = random.uniform(-step_size, step_size)
        new_value = current_point[i] + perturbation
        if new_value < lower_bound:
            new_value = lower_bound
        elif new_value > upper_bound:
            new_value = upper_bound
        neighbor.append(new_value)
    return neighbor
def objective(point):
    sum_of_squares = 0
    for value in point:
        sum_of_squares += value**2
    return sum_of_squares
bounds = [(-5, 5)] * 2  
n_iterations = 10000  
step_size = 0.1  
init_temp = 100  
cooling_rate = 0.99 
best_point, best_value = simulated_annealing(objective, bounds, n_iterations, step_size, init_temp, cooling_rate)
print("Best point:", best_point)
print("Best value:", best_value)
