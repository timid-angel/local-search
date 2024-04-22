from tsp_solver import solve_tsp, stringify_solution

ga_ans, ga_val = solve_tsp("ga", "data.txt")
# hc_ans = solve_tsp("hc", "data.txt")
# sa_ans = solve_tsp("sa", "data.txt")

print("Genetic Algorithm")
print(stringify_solution(ga_ans))
print(ga_val)

# print("\nHill-climbing")
# print(hc_ans)

# print("\nSimulated Annealing")
# print(sa_ans)
