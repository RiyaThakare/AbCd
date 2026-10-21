from collections import deque

def successors(state):
    result = []

    for i in range(len(state)):
        block = state[i][-1]

        for j in range(len(state)):
            if i != j:
                new = [list(s) for s in state]
                new[i].pop()
                new[j].append(block)
                result.append(tuple(tuple(s) for s in new if s))

        new = [list(s) for s in state]
        new[i].pop()
        new.append([block])
        result.append(tuple(tuple(s) for s in new if s))

    return result

def bfs(start, goal):
    q = deque([(start, [start])])
    visited = {start}

    while q:
        state, path = q.popleft()

        if state == goal:
            return path

        for s in successors(state):
            if s not in visited:
                visited.add(s)
                q.append((s, path + [s]))

    return None

start = (tuple(input("Enter initial stack: ").upper()),)
goal = (tuple(input("Enter goal stack: ").upper()),)

ans = bfs(start, goal)

if ans:
    for i, state in enumerate(ans):
        print("Step", i, ":", state)
    print("Number of moves:", len(ans) - 1)
else:
    print("No solution found")
