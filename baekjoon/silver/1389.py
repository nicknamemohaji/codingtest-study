import sys
readline = lambda: sys.stdin.readline().strip()

N, M, = map(int, readline().split())
graph = [[sys.maxsize]  * N for _ in range(N)]
for _ in range(M):
    a, b, = map(int, readline().split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1
for i in range(N):
    graph[i][i] = 0

for m in range(N):
    for s in range(N):
        for e in range(N):
            graph[s][e] = min(graph[s][e], graph[s][m] + graph[m][e])

costs = [(sum(line), idx) for line, idx in zip(graph, range(N))]
print(min(costs)[1] + 1)