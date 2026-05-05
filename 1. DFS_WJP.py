# Water Jug Problem using Python (BFS Approach)

from collections import deque

# Function to solve Water Jug Problem
def water_jug_problem(jug1, jug2, target):
    
    visited = set()
    queue = deque()

    # Initial state (0,0)
    queue.append((0, 0))
    visited.add((0, 0))

    while queue:
        x, y = queue.popleft()

        print((x, y))

        # Check if target is achieved
        if x == target or y == target:
            print("\nTarget reached!")
            return

        # Possible next states
        possible_states = [
            (jug1, y),  # Fill Jug1
            (x, jug2),  # Fill Jug2
            (0, y),     # Empty Jug1
            (x, 0)      # Empty Jug2
        ]

        # Pour Jug1 -> Jug2
        transfer = min(x, jug2 - y)
        possible_states.append((x - transfer, y + transfer))

        # Pour Jug2 -> Jug1
        transfer = min(y, jug1 - x)
        possible_states.append((x + transfer, y - transfer))

        # Add unvisited states
        for state in possible_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)

# Driver Code
jug1_capacity = 4
jug2_capacity = 3
target = 2

water_jug_problem(jug1_capacity, jug2_capacity, target)
