import heapq
import sys
readline = lambda : sys.stdin.readline().strip()

V, E, = map(int, readline().split())
K = int(readline())
graph = list(list() for _ in range(V))
for _ in range(E):
    u, v, w, = map(int, readline().split())
    u, v, = u - 1, v - 1
    graph[u].append([w, v])

costs = [sys.maxsize] * V
queue = [(0, K - 1)]
while queue:
    cost, dst, = heapq.heappop(queue)
    if costs[dst] < cost:
        continue
    costs[dst] = cost
    for w, v, in graph[dst]:
        next_cost = cost + w
        if costs[v] < next_cost:
            continue
        costs[v] = next_cost
        heapq.heappush(queue, (next_cost, v))

for cost in costs:
    print(cost if cost != sys.maxsize else "INF")