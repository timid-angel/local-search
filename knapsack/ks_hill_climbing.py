import random

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


def hill_climbing(bags: list, maxWeight: int):
    current_solution = generate_solution(len(bags))

    while True:
        neighbors = generate_neighbors(current_solution)
        best = max(neighbors, key=lambda s: objective_fxn(bags, s, maxWeight))

        # stop if a local maxima has been found
        if objective_fxn(bags, best, maxWeight) <= objective_fxn(bags, current_solution, maxWeight):
            break 
        
        current_solution = best
    
    return (current_solution, objective_fxn(bags, current_solution, maxWeight))
