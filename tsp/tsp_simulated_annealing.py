import random
import numpy as np

from graph import Graph

def objective_fxn(solution: list):
    score = 0
    for i in range(1, len(solution)):
        score += Graph.getDistance(solution[i], solution[i - 1])
    
    # the distance to get back to the initial point
    score += Graph.getDistance(solution[0], solution[-1])

    return score


def generate_neighbors(solution: list):
    neighbors = []
    for i in range(len(solution)):
        if i != 1:
            nb = solution[:]
            nb[i], nb[1] = nb[1], nb[i]
            neighbors.append(nb)
    
    return neighbors


def generate_solution(graph: Graph):
    nodes = set(graph.nodes)
    start_point = random.choice(graph.nodes)
    ans = [start_point]
    nodes.remove(start_point)

    for __ in range(len(nodes)):
        rand = random.choice(list(nodes))
        nodes.remove(rand)
        ans.append(rand)
    
    return ans


def simulated_annealing(graph: Graph, cooling_factor: float, initial_T: float, min_T: float):
    current_solution = best_solution = generate_solution(graph)
    T = initial_T

    while True:
        T *= cooling_factor
        if T < min_T:
            break

        neighbors = generate_neighbors(current_solution)
        next_solution = random.choice(neighbors)
        delta_E = objective_fxn(next_solution) - objective_fxn(current_solution)

        if objective_fxn(next_solution) < objective_fxn(best_solution):
            best_solution = next_solution

        if delta_E < 0:
            current_solution = next_solution
        
        elif random.random() < np.exp(-delta_E / T):
            current_solution = next_solution
    
    return (current_solution, objective_fxn(current_solution))
