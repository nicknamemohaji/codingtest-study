import heapq
import sys
readline = lambda: sys.stdin.readline().strip()

N, M, K, X, = map(int, readline().split())

graph = [list() for _ in range(N)]
for _ in range(M):
    src, dst, = map(int, readline().split())
    graph[src - 1].append(dst - 1)

queue = [(0, X - 1)]
costs = [sys.maxsize] * N
costs[X - 1] = 0
while queue:
    cost, src = heapq.heappop(queue)
    if costs[src] < cost:
        continue
    for dst in graph[src]:
        if costs[dst] <= cost + 1:
            continue
        costs[dst] = cost + 1
        heapq.heappush(queue, (cost + 1, dst))

is_printed = False
for i in range(N):
    if costs[i] != K:
        continue
    print(i + 1)
    is_printed = True
if not is_printed:
    print(-1)
