import random
import math

# return an array of a random solution 
def generate_solutions(sackCount: int):
    sol = []
    for i in range(sackCount):
        sol.append(random.choice([0, 1]))
    
    return sol


def generate_generation(size: int, bagSize: int):
    return [generate_solutions(bagSize) for _ in range(size)]


def fitness_function(bags: list, maxWeight: int, solution: list):
    weight = value = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            weight += bags[i].weight
            value += bags[i].value
    
    return -1 if weight > maxWeight else value


def parent_selection(generation: list, bags: list, maxWeight: int):
    fitness_values = []
    for i in range(len(generation)):
        fitness = fitness_function(bags, maxWeight, generation[i])
        fitness_values.append(fitness)

    return random.choices(population=generation, weights=fitness_values, k=2)


def crossover(solution1: list, solution2: list):
    cutoff = math.floor(random.random() * len(solution1))
    return (solution1[:cutoff] + solution2[cutoff:]), (solution2[:cutoff] + solution1[cutoff:])


def mutate(solution: int, rate: float = 0.5):
    if random.random() < rate:
        idx = math.floor(random.random() * len(solution))
        solution[idx] = 0 if solution[idx] == 1 else 1


def genetic_algorithm(bags: list, maxWeight: int, generation_limit: int, generation_size: int):
    gen = generate_generation(generation_size, len(bags))

    for _ in range(generation_limit):
        gen.sort(key=lambda ans: fitness_function(bags, maxWeight, ans), reverse=True)

        # maintain the top 2 to transfer them directly to the next genertion
        next_gen = gen[:2]
        while len(next_gen) < len(gen):
            parent1, parent2 = parent_selection(gen, bags, maxWeight)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            next_gen.append(child1)
            next_gen.append(child2)
        
        # go to the next generation of solutions
        gen = next_gen
    
    gen.sort(key=lambda ans: fitness_function(bags, maxWeight, ans), reverse=True)

    return gen