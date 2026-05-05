# A* Search Algorithm in Python

from queue import PriorityQueue

# Graph representation
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 6)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 2,
    'G': 0
}

# A* Algorithm
def astar(start, goal):

    pq = PriorityQueue()
    pq.put((0, start))

    cost = {start: 0}
    parent = {start: None}

    while not pq.empty():

        current = pq.get()[1]

        if current == goal:
            break

        for neighbor, weight in graph[current]:

            new_cost = cost[current] + weight

            if neighbor not in cost or new_cost < cost[neighbor]:

                cost[neighbor] = new_cost

                priority = new_cost + heuristic[neighbor]

                pq.put((priority, neighbor))

                parent[neighbor] = current

    # Reconstruct path
    path = []
    node = goal

    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()

    print("Shortest Path :", path)
    print("Total Cost :", cost[goal])

# Driver Code
astar('A', 'G')
