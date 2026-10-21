from collections import deque

def hanoi(n):
    start = tuple([0] * n)
    goal = tuple([2] * n)

    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            print("Solution: ")
            for move in path:
                print(move)
            print("Total moves: ", len(path))
            return

        pegs = [[], [], []]

        for disk, peg in enumerate(state):
            pegs[peg].append(disk)

        for i in range(3):
            if not pegs[i]:
                continue

            disk = pegs[i][0]

            for j in range(3):
                if i == j:
                    continue

                if not pegs[j] or disk < pegs[j][0]:
                    new_state = list(state)
                    new_state[disk] = j
                    new_state = tuple(new_state)

                    if new_state not in visited:
                        visited.add(new_state)
                        move = f"Move disk {disk +1} from peg {i+1} to peg {j+1}"
                        queue.append((new_state, path + [move]))

n = int(input("Enter number of disks: "))
hanoi(n)