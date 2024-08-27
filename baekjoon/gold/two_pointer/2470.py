import sys
readline = sys.stdin.readline

N = int(input())
solutions = list(map(int, readline().strip().split()))
solutions.sort()

last_compare = (solutions[0] + solutions[N - 1], 0, N - 1)

left, right, = 0, N - 1
while left < right:
	conecentration = solutions[left] + solutions[right]
	if abs(conecentration) < abs(last_compare[0]):
		last_compare = (solutions[left] + solutions[right], left, right)
	if conecentration > 0:
		right -= 1
	else:
		left += 1

print(solutions[last_compare[1]], solutions[last_compare[2]])