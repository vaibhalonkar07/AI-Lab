
# Model-Based Agent for Grid Navigation

grid = [
    ['S', '.', '#', '.'],
    ['.', '.', '#', '.'],
    ['#', '.', '.', 'G'],
    ['.', '.', '.', '.']
]

# S = Start, G = Goal, # = Obstacle, . = Empty

position = (0, 0)
internal_state = set()

def agent(position):
    internal_state.add(position)

    x, y = position
    moves = [
        (x, y + 1),  # Right
        (x + 1, y),  # Down
        (x, y - 1),  # Left
        (x - 1, y)   # Up
    ]

    for nx, ny in moves:
        if (0 <= nx < len(grid) and
            0 <= ny < len(grid[0]) and
            grid[nx][ny] != '#' and
            (nx, ny) not in internal_state):
            return (nx, ny)

    return None

# Run the agent
while position != (2, 3):
    print("Current Position:", position)
    next_position = agent(position)

    if next_position is None:
        print("No unvisited path found!")
        break

    position = next_position

print("Goal Reached!" if position == (2, 3) else "Goal Not Reached")
