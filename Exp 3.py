from collections import deque

capacity = (4, 3)
start = (0, 0)
goal = 2

q = deque([start])
visited = {start}

while q:
    a, b = q.popleft()
    print(a, b)

    if a == goal or b == goal:
        print("Goal reached")
        break

    pour_ab = min(a, capacity[1] - b)
    pour_ba = min(b, capacity[0] - a)

    states = [
        (capacity[0], b),
        (a, capacity[1]),
        (0, b),
        (a, 0),
        (a - pour_ab, b + pour_ab),
        (a + pour_ba, b - pour_ba)
    ]

    for s in states:
        if s not in visited:
            visited.add(s)
            q.append(s)
