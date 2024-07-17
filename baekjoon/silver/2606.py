N = int(input())
relations = int(input())

graph = [[False for _ in range(N)] for _ in range(N)]

for _ in range(relations):
	i, j = map(int, input().split())
	graph[i - 1][j - 1] = True
	graph[j - 1][i - 1] = True

queue = [0]
visited = set()
infected = set()
while len(queue) != 0:
	current_row = queue.pop(0)
	visited.add(current_row)
	queue.extend([index for index in range(N)
		if graph[current_row][index] == True
		and index not in visited
		])
	infected.add(current_row)

print(len(infected) - 1)