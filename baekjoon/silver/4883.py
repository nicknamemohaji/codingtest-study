import sys
readline = sys.stdin.readline

tests = 0
while True:
	tests += 1
	N = int(readline().strip())
	if N == 0:
		break
	graph = list()
	for _ in range(N):
		graph.append(list(map(int, readline().strip().split())))
	
	costs = [graph[0][1], graph[0][1], graph[0][1] + graph[0][2]]
	for line in graph[1:]:
		line[0] += min(costs[0], costs[1])
		line[1] += min(costs[0], costs[1], costs[2], line[0])
		line[2] += min(costs[1], costs[2], line[1])
		costs = line

	print(f"{tests}. {costs[1]}")