from collections import deque

grid = [
    ['S', '.', '#'],
    ['.', '.', '#'],
    ['#', '.', 'G']
]

start = (0, 0)
goal = (2, 2)

queue = deque([(start, [start])])
visited = {start}

while queue:
    (r, c), path = queue.popleft()

    if (r, c) == goal:
        print("Path:", path)
        break

    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr, nc = r + dr, c + dc

        if (0 <= nr < 3 and 0 <= nc < 3
            and grid[nr][nc] != '#'
            and (nr, nc) not in visited):

            visited.add((nr, nc))
            queue.append(((nr, nc), path + [(nr, nc)]))
