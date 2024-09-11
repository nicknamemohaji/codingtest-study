import sys
readline = lambda: sys.stdin.readline().strip()

N = int(readline())
graph = [[False] * N for _ in range(N)]
visited = [False] * N

for src in range(N - 1):
    readline()
    for dst in map(int, readline().split()):
        graph[src][dst - 1] = True

def dfs(src: int) -> None:
    global N, visited, graph
    if src == N - 1:
        return
    if visited[src]:
        print("CYCLE")
        sys.exit(0)
    visited[src] = True
    for dst in range(N):
        if not graph[src][dst]:
            continue
        dfs(dst)
    visited[src] = False

dfs(0)
print("NO CYCLE")
