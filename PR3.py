import heapq

start = (1,2,3,
         0,4,6,
         7,5,8)


goal = (1,2,3,
        4,5,6,
        7,8,0)

def manhattan(state):
    d = 0
    for i, tile in enumerate(state):
        if tile:
            r1, c1 = divmod(i, 3)
            j = goal.index(tile)
            r2, c2 = divmod(j, 3)
            d += abs(r1-r2) + abs(c1-c2)
    return d

def neighbors(state):
    result = []
    b = state.index(0)
    r, c = divmod(b, 3)

    for dr, dc, move in [(-1,0,"Up"), (1,0,"Down"),
                         (0,-1,"Left"), (0,1,"Right")]:
        nr, nc = r+dr, c+dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            nb = nr*3 + nc
            s = list(state)
            s[b], s[nb] = s[nb], s[b]
            result.append((tuple(s), move))

    return result

def a_star(start):
    pq = [(manhattan(start), 0, start)]
    parent = {start: None}
    move = {start: None}
    cost = {start: 0}

    while pq:
        f, g, current = heapq.heappop(pq)

        if current == goal:
            path = []
            while current:
                path.append((current, move[current]))
                current = parent[current]
            return path[::-1]

        for nxt, m in neighbors(current):
            new_g = g + 1

            if nxt not in cost or new_g < cost[nxt]:
                cost[nxt] = new_g
                parent[nxt] = current
                move[nxt] = m
                heapq.heappush(pq, (new_g + manhattan(nxt), new_g, nxt))

solution = a_star(start)

for i, (state, move) in enumerate(solution):
    print(f"\nStep {i}: {move}")
    print(state[:3])
    print(state[3:6])
    print(state[6:9])