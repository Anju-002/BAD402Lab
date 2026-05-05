# AO* Search Algorithm in Python

# Graph representation
graph = {
    'A': [['B', 'C'], ['D']],
    'B': [['E'], ['F']],
    'C': [['G']],
    'D': [['H']],
    'E': [],
    'F': [],
    'G': [],
    'H': []
}

# Heuristic values
H = {
    'A': 1,
    'B': 6,
    'C': 2,
    'D': 12,
    'E': 2,
    'F': 1,
    'G': 0,
    'H': 0
}

# Cost of each node
cost = {
    'A': 1,
    'B': 1,
    'C': 1,
    'D': 1,
    'E': 0,
    'F': 0,
    'G': 0,
    'H': 0
}

# Function to calculate minimum cost
def minimum_cost_child(node):

    if len(graph[node]) == 0:
        return H[node]

    min_cost = float('inf')

    for child_group in graph[node]:

        current_cost = 0

        for child in child_group:
            current_cost += H[child] + cost[child]

        min_cost = min(min_cost, current_cost)

    H[node] = min_cost
    return H[node]

# AO* Algorithm
def ao_star(start):

    print("Updated Cost Values:\n")

    changed = True

    while changed:

        changed = False

        for node in reversed(list(graph.keys())):

            old_cost = H[node]

            new_cost = minimum_cost_child(node)

            if old_cost != new_cost:
                changed = True

    for node in H:
        print(node, ":", H[node])

# Driver Code
ao_star('A')
