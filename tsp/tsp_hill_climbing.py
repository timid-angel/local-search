import random

from tsp.graph import Graph

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


def hill_climbing(graph: Graph):
    current_solution = generate_solution(graph)

    while True:
        neighbors = generate_neighbors(current_solution)
        best = min(neighbors, key=lambda s: objective_fxn(s))

        # stop if a local minima has been found
        if objective_fxn(best) >= objective_fxn(current_solution):
            break 
        
        current_solution = best
    
    return (current_solution, objective_fxn(current_solution))
