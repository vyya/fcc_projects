my_graph = {'A':[('B', 3),('D', 1)], 'B':[('A', 3),('C', 4)], 'C':[('B', 4),('D', 7)], 'D':[('A', 1),('C', 7)]}

def shortest_path(graph, start):
    # Create a list of unvisited nodes using list constructor
    unvisited = list(graph)
    distances = {}
    # Create a dictionary of paths using dictionary comprehension
    paths = {key: [] for key in graph}
    print(f'Unvisited: {unvisited}\nDistances: {distances}')
shortest_path(my_graph, 'A')
