import heapq

goal = (
    1,2,3,
    8,0,4,
    7,6,5
)

start = (
    8,1,3,
    7,0,4,
    6,2,5
)

def heuristic(state):
    h = 0
    for i in range(9):
        if state[i] != 0:
            goal_pos = goal.index(state[i])
            h += abs(i//3 - goal_pos // 3)
            h += abs(i%3 - goal_pos % 3)
    return h

def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    row = zero // 3
    col = zero % 3
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        r = row + dr
        c = col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            new_zero = r * 3 + c
            new_state = list(state)
            new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]
            neighbors.append(tuple(new_state))
    return neighbors


def a_star(start):
    OPEN = []
    CLOSED = set()

    parent = {start: None}
    g = {start: 0}

    # Store (f, -depth, state)
    heapq.heappush(
        OPEN, (heuristic(start), 0, start)
    )
    while OPEN:
        f, neg_depth, state = heapq.heappop(OPEN)

        if state in CLOSED:
            continue

        CLOSED.add(state)

        # Goal test
        if state == goal:
            path = []

            while state is not None:
                path.append(state)
                state = parent[state]

            return path[::-1]

        for next_state in get_neighbors(state):
            new_g = g[state] + 1
            if new_g < g.get(next_state, float("inf")):
                g[next_state] = new_g
                parent[next_state] = state

                CLOSED.discard(next_state)

                new_f = new_g + heuristic(next_state)

                heapq.heappush(
                    OPEN, (new_f, -new_g, next_state)
                )
    return None


solution = a_star(start)
if solution:
    print("Solution found!")
    print("Number of moves:", len(solution) - 1)
    for state in solution:
            print(state[0:3])
            print(state[3:6])
            print(state[6:9])
            print()
else:
            print("No solution found!")