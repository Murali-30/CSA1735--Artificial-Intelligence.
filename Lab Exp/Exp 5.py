from collections import deque

start = (3, 3, 0)
goal = (0, 0, 1)
moves = [(1, 0), (2, 0), (0, 1),
         (0, 2), (1, 1)]

q = deque([(start, [])])
visited = {start}

while q:
    state, path = q.popleft()
    m, c, boat = state

    if state == goal:
        for s in path + [state]:
            print(s)
        break

    for dm, dc in moves:
        if boat == 0:
            nm, nc = m - dm, c - dc
            nb = 1
        else:
            nm, nc = m + dm, c + dc
            nb = 0

        if not (0 <= nm <= 3 and 0 <= nc <= 3):
            continue

        rm, rc = 3 - nm, 3 - nc

        if ((nm == 0 or nm >= nc) and
            (rm == 0 or rm >= rc)):
            ns = (nm, nc, nb)

            if ns not in visited:
                visited.add(ns)
                q.append((ns, path + [state]))
