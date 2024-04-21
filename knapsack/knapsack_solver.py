from ks_genetic_algorithm import genetic_algorithm
from bag_item import BagItem


def solve_knapsack(algorithm: str, file_name: str):
    file = open(file_name)
    maxWeight = int(file.readline().strip())
    bags = []

    file.readline() # ignore the second line of the file
    line = file.readline()
    while line:
        item_arr = list(map(lambda x: x.strip(), line.split(",")))
        count = 1 if len(item_arr) == 3 else int(item_arr[3])

        for i in range(count):
            bag_item = BagItem(item_arr[0], float(item_arr[1]), float(item_arr[2]))
            bags.append(bag_item)

        line = file.readline()

    if algorithm == "ga":
        generation_limit = 20
        generation_size = 10
        ans = genetic_algorithm(bags, maxWeight, generation_limit, generation_size)
        return ans
