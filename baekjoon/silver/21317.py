from collections import deque

N = int(input())
costs = list()
for _ in range(N - 1):
	costs.append(list(map(int, input().split())))
K = int(input())

prices = [[-1, -1] for _ in range(N)]
prices[0] = (0, 0)

queue = deque([(0, 0, False)])
if N == 1:
	queue.pop()

while queue:
	current_location, current_cost, current_bigjump, = queue.popleft()
	move_costs = costs[current_location]
	for next_location, next_cost, next_bigjump, in \
	 (
		(current_location + 1, current_cost + move_costs[0], False),
		(current_location - 1, current_cost + move_costs[0], False),
		(current_location + 2, current_cost + move_costs[1], False),
		(current_location - 2, current_cost + move_costs[1], False),
		(current_location + 3, current_cost + K, True),
		(current_location - 3, current_cost + K, True),
	 ):
		if next_location < 0 or next_location >= N:
			continue
		if next_bigjump and current_bigjump:
			continue
		next_bigjump |= current_bigjump
		if prices[next_location][next_bigjump] != -1 and prices[next_location][next_bigjump] < next_cost:
			continue
		prices[next_location][next_bigjump] = next_cost
		if next_location != N - 1:
			queue.append((next_location, next_cost, next_bigjump))

if prices[-1][1] == -1:
	prices[-1][1] = prices[-1][0]
print(min(prices[-1]))
