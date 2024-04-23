from tsp_solver import solve_tsp, stringify_solution

ga_ans, ga_val = solve_tsp("ga", "data.txt")
hc_ans, hc_val = solve_tsp("hc", "data.txt")
sa_ans, sa_val = solve_tsp("sa", "data.txt")

print("Genetic Algorithm")
print(stringify_solution(ga_ans))
print(ga_val)

print("\nHill-climbing")
print(stringify_solution(hc_ans))
print(hc_val)

print("\nSimulated Annealing")
print(stringify_solution(sa_ans))
print(sa_val)
