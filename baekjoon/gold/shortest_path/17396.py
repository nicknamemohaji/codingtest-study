import heapq
import sys
readline = lambda : sys.stdin.readline().strip()
INF = sys.maxsize

N, M, = map(int, readline().split())
visibility = list(map(int, readline().split()))
graph = [list() for _ in range(N)]
for _ in range(M):
    a, b, t, = map(int, readline().split())
    if (visibility[a] == 1 and a != N - 1) \
        or (visibility[b] == 1 and b != N - 1):
        continue
    graph[a].append((t, b))
    graph[b].append((t, a))
costs = [INF] * N
queue = [(0, 0)]
costs[0] = 0
while queue:
    cost, dst, = heapq.heappop(queue)
    if costs[dst] < cost:
        continue
    for t, b, in graph[dst]:
        next_cost = cost + t
        if costs[b] <= next_cost:
            continue
        costs[b] = next_cost
        heapq.heappush(queue, (next_cost, b))

print(costs[-1] if costs[-1] != INF else -1)
