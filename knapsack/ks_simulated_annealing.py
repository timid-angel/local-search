import random
import numpy as np

def objective_fxn(bags: list, solution: list, maxWeight: int):
    weight = value = 0
    for i in range(len(bags)):
        if solution[i] == 1:
            weight += bags[i].weight
            value += bags[i].value
    
    return -1 if weight > maxWeight else value


def generate_neighbors(solution: list):
    nbs = []
    for i in range(len(solution)):
        new_val = 0 if solution[i] == 1 else 1
        nb = solution[:i] + [new_val] + solution[i + 1:]
        nbs.append(nb)
    
    return nbs


def generate_solution(size: int):
    sol = []
    for i in range(size):
        sol.append(random.choice([0, 1]))
    
    return sol


def simulated_annealing(bags: list, maxWeight: int, cooling_factor: float, initial_T: float, min_T: float):
    current_solution = best_solution = generate_solution(len(bags))
    T = initial_T

    while True:
        T *= cooling_factor
        if T < min_T:
            break

        neighbors = generate_neighbors(current_solution)
        next_solution = random.choice(neighbors)
        delta_E = objective_fxn(bags, next_solution, maxWeight) - objective_fxn(bags, current_solution, maxWeight)

        if objective_fxn(bags, next_solution, maxWeight) > objective_fxn(bags, best_solution, maxWeight):
            best_solution = next_solution

        if delta_E > 0:
            current_solution = next_solution
        
        elif random.random() < np.exp(delta_E / T):
            current_solution = next_solution
    
    return (current_solution, objective_fxn(bags, current_solution, maxWeight))
