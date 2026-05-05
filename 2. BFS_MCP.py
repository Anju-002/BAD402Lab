# Missionaries and Cannibals Problem using BFS

from collections import deque

# Check whether a state is valid
def is_valid(m, c):
    # Missionaries should not be outnumbered
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False

    if (m > 0 and m < c):
        return False

    if ((3 - m) > 0 and (3 - m) < (3 - c)):
        return False

    return True

# BFS function
def bfs():
    start = (3, 3, 1)   # (Missionaries, Cannibals, Boat)
    goal = (0, 0, 0)

    queue = deque()
    queue.append((start, []))

    visited = set()

    while queue:
        (m, c, b), path = queue.popleft()

        if (m, c, b) in visited:
            continue

        visited.add((m, c, b))

        path = path + [(m, c, b)]

        # Goal state reached
        if (m, c, b) == goal:
            print("Solution Path:\n")
            for state in path:
                print(state)
            return

        # Possible boat moves
        moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

        for mm, cc in moves:

            if b == 1:  # Boat on left side
                new_state = (m - mm, c - cc, 0)
            else:       # Boat on right side
                new_state = (m + mm, c + cc, 1)

            if is_valid(new_state[0], new_state[1]):
                queue.append((new_state, path))

# Driver Code
bfs()
