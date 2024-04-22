import random
import math

from knapsack_solver import solve_knapsack

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


generate_knapsack_list(10)
generate_knapsack_list(15)
generate_knapsack_list(20)

ga_ans10 = solve_knapsack("ga", "item_list_10.txt")
ga_ans15 = solve_knapsack("ga", "item_list_15.txt")
ga_ans20 = solve_knapsack("ga", "item_list_20.txt")

hc_ans10 = solve_knapsack("ga", "item_list_10.txt")
hc_ans15 = solve_knapsack("ga", "item_list_15.txt")
hc_ans20 = solve_knapsack("ga", "item_list_20.txt")

print("10 items:\n", ga_ans10, "\n")
print("15 items:\n", ga_ans15, "\n")
print("20 items:\n", ga_ans20, "\n")

print("10 items:\n", hc_ans10, "\n")
print("15 items:\n", hc_ans15, "\n")
print("20 items:\n", hc_ans20, "\n")
