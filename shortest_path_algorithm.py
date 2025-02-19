my_graph = {'A':[('B', 3),('D', 1)], 'B':[('A', 3),('C', 4)], 'C':[('B', 4),('D', 7)], 'D':[('A', 1),('C', 7)]}

def shortest_path(graph, start):
    # Create a list of unvisited nodes using list constructor
    unvisited = list(graph)
    # create a distionary of distances using dictionary comprehension
    distances = {node: 0 if node == start else float('inf') for node in graph}
    # Create a dictionary of paths using dictionary comprehension
    paths = {key: [] for key in graph}
    # Add the starting point to the paths dictionary
    paths[start].append(start)
    print(f'Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}')
shortest_path(my_graph, 'A')
