maze = [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 1, 0],
    [0, 0, 0, 0]
]

rows = len(maze)
cols = len(maze[0])

visited = set()

def dfs(x, y):
    # Check boundaries
    if x < 0 or y < 0 or x >= rows or y >= cols:
        return False

    # Check wall
    if maze[x][y] == 1:
        return False

    # Check if already visited
    if (x, y) in visited:
        return False

    print("Visited:", (x, y))

    # Check if goal is reached
    if (x, y) == (3, 3):
        print("\nGoal Reached!")
        return True

    visited.add((x, y))

    # Explore down, up, right, and left
    if dfs(x + 1, y):
        return True

    if dfs(x - 1, y):
        return True

    if dfs(x, y + 1):
        return True

    if dfs(x, y - 1):
        return True

    return False

# Start DFS from (0, 0)
dfs(0, 0)