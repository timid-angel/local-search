import random
import math

from tsp.graph import Graph


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


def generate_generation(graph: Graph, size: int):
    return [generate_solution(graph) for _ in range(size)]


def fitness_function(solution: list):
    score = 0
    for i in range(1, len(solution)):
        score += Graph.getDistance(solution[i], solution[i - 1])
    
    # the distance to get back to the initial point
    score += Graph.getDistance(solution[0], solution[-1])

    return score


def parent_selection(generation: list):
    fitness_values = []
    for solution in generation:
        score = fitness_function(solution)
        fitness = 1 / score if score > 0 else 1
        fitness_values.append(fitness * 1000)
    
    return random.choices(population=generation, weights=fitness_values, k=2)


def crossover(solution1: list, solution2: list):
    def pmx(s, t):
        cutoff = math.floor(random.random() * len(s))
        child = s[:]

        for idx in range(cutoff):
            matching_idx = 0
            for j in range(len(child)):
                if child[j] == t[idx]:
                    matching_idx = j
                    break
            
            child[matching_idx], child[idx] = child[idx], child[matching_idx]
        
        return child

    return pmx(solution1, solution2), pmx(solution2, solution1)

def mutate(solution: list, rate: float = 0.5):
    if random.random() < rate:
        idx1 = math.floor(random.random() * len(solution))
        idx2 = math.floor(random.random() * len(solution))

        solution[idx1], solution[idx2] = solution[idx2], solution[idx1]


def genetic_algorithm(graph: Graph, generation_limit: int, generation_size: int):
    gen = generate_generation(graph, generation_size)

    for __ in range(generation_limit):
        gen.sort(key=lambda s: fitness_function(s))

        nxt_gen = gen[:2]
        while len(nxt_gen) < len(gen):
            parent1, parent2 = parent_selection(gen)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            nxt_gen.append(child1)
            nxt_gen.append(child2)
        
        gen = nxt_gen

    solution = max(gen, key=lambda s: -fitness_function(s))

    return solution, fitness_function(solution)