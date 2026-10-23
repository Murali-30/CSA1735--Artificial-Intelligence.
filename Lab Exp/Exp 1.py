from collections import deque

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

q = deque([(start, [])])
visited = {start}

while q:
    state, path = q.popleft()

    if state == goal:
        print("Solution:")
        for s in path + [state]:
            print(s[:3], s[3:6], s[6:])
        break

    z = state.index(0)
    for move in [-3, 3, -1, 1]:
        n = z + move

        if 0 <= n < 9:
            if abs(move) == 1 and z // 3 != n // 3:
                continue

            new = list(state)
            new[z], new[n] = new[n], new[z]
            new = tuple(new)

            if new not in visited:
                visited.add(new)
                q.append((new, path + [state]))
