import argparse

from tsp_solver import solve_tsp

parser = argparse.ArgumentParser(description="Knapsack Problem")
parser.add_argument("--algorithm", help="algorithm to run")
parser.add_argument("--file", help="file containing a valid set of data")

args = parser.parse_args()
algorithm = args.algorithm
file_name = args.file

if algorithm not in ['ga', 'hc', 'sa']:
    raise ValueError('Invalid algorithm option: Input must be either "ga", "hc" or "sa"')

print(solve_tsp(algorithm, file_name))
