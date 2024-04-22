from graph import Graph, Node
from tsp_genetic_algorithm import genetic_algorithm


def stringify_solution(solution):
    s = ""
    for node in solution:
        s += f"{node.val} => "
    
    s += solution[0].val

    return s


def solve_tsp(algorithm: str, file_name: str = "data.txt"):
    file = open(f"./tsp/{file_name}", "r")
    graph = Graph()

    line = file.readline()
    while line:
        line = file.readline()
        if line.strip():
            entry = line.split("    ")
            city, lat, long = entry[0], float(entry[1].strip()), float(entry[2].strip())
            city_node = Node(city, lat, long)
            graph.addNode(city_node)

    file.close()

    solution, weight = None, None

    if algorithm == "ga":
        generation_limit = 20
        generation_size = 10
        solution, weight = genetic_algorithm(graph, generation_limit, generation_size)
    

    return solution, weight
        