
from collections import deque

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def bfs(start):
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()
        path = path + [state]

        if state == goal:
            return path

        b = state.index(0)

        for n in [b-3, b+3, b-1, b+1]:
            if 0 <= n < 9 and abs(n//3 - b//3) + abs(n%3 - b%3) == 1:
                s = list(state)
                s[b], s[n] = s[n], s[b]
                s = tuple(s)

                if s not in visited:
                    visited.add(s)
                    queue.append((s, path))

    return None

path = bfs(start)

for step, state in enumerate(path):
    print("Step", step)
    print(state[:3])
    print(state[3:6])
    print(state[6:])
    print()
