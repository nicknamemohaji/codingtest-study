N = int(input())

houses = list()
for _ in range(N):
	houses.append(list(map(int, input().split())))

costs = [0] * 3
for house in houses:
	r, g, b, = house
	new_cost = [
		r + min(costs[1], costs[2]),
		g + min(costs[0], costs[2]),
		b + min(costs[0], costs[1])
		]
	costs = new_cost

print(min(costs))