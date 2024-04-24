import time

from tsp.tsp_solver import solve_tsp

def run_algorithms(file_name: str):
    results = {
        "Genetic Algorithm": [[], []],
        "Hill Climbing": [[], []],
        "Simulated Annealing": [[], []]
    }

    graphs = {
        "Genetic Algorithm": [[], []],
        "Hill Climbing": [[], []],
        "Simulated Annealing": [[], []]
        }

    for _ in range(10):
        gst = time.time()
        g_graph, ga_ans, ga_val = solve_tsp("ga", file_name)
        gen = time.time()

        hst = time.time()
        h_graph, hc_ans, hc_val = solve_tsp("hc", file_name)
        hen = time.time()

        sst = time.time()
        s_graph, sa_ans, sa_val = solve_tsp("sa", file_name)
        sen = time.time()

        results["Genetic Algorithm"][0].append(gen - gst)
        results["Genetic Algorithm"][1].append(ga_val)

        results["Hill Climbing"][0].append(hen - hst)
        results["Hill Climbing"][1].append(hc_val)

        results["Simulated Annealing"][0].append(sen - sst)
        results["Simulated Annealing"][1].append(sa_val)

        graphs["Genetic Algorithm"] = g_graph
        graphs["Hill Climbing"] = h_graph
        graphs["Simulated Annealing"] = s_graph
    
    return results, graphs


tsp_8, graph_8 = run_algorithms("data_8.txt")
tsp_16, graph_16 = run_algorithms("data_16.txt")
tsp_20, graph_20 = run_algorithms("data_20.txt")
