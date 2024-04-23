import random
import math
import time

from knapsack.knapsack_solver import solve_knapsack

def generate_name(char_count: int):
    name = ""
    for _ in range(char_count):
        unicode = math.floor(random.random() * 26) + 97
        name += chr(unicode)
    
    return name.title()


def generate_knapsack_list(itemCount: int):
    file = open(f"item_list_{itemCount}.txt", "+w")
    maxWeight = math.floor((random.random() * 50)) + 30
    file.writelines(str(maxWeight) + "\n")
    file.writelines("item,weight,value,n_items\n")

    for _ in range(itemCount):
        name = generate_name(5)
        weight = round(random.random() * 5, 1) + 0.1
        value = math.floor(random.random() * 1000) + 1
        file.writelines(f"{name},{weight},{value}\n")


def run_algorithms(item_count: int):
    results = {
        "Genetic Algorithm": [[], []],
        "Hill Climbing": [[], []],
        "Simulated Annealing": [[], []]
    }

    for _ in range(10):
        generate_knapsack_list(item_count)

        gst = time.time()
        ga_ans, ga_val = solve_knapsack("ga", f"item_list_{item_count}.txt")
        gen = time.time()

        hst = time.time()
        hc_ans, hc_val = solve_knapsack("hc", f"item_list_{item_count}.txt")
        hen = time.time()

        sst = time.time()
        sa_ans, sa_val = solve_knapsack("sa", f"item_list_{item_count}.txt")
        sen = time.time()

        results["Genetic Algorithm"][0].append(gen - gst)
        results["Genetic Algorithm"][1].append(ga_val)

        results["Hill Climbing"][0].append(hen - hst)
        results["Hill Climbing"][1].append(hc_val)

        results["Simulated Annealing"][0].append(sen - sst)
        results["Simulated Annealing"][1].append(sa_val)


    return results


knapsack_10 = run_algorithms(10)
knapsack_15 = run_algorithms(15)
knapsack_20 = run_algorithms(20)
