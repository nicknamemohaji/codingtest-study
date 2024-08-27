import sys
readline = sys.stdin.readline

N = int(input())
solutions = list(map(int, readline().strip().split()))
solutions.sort()

last_compare = (1000000000 * 3 + 1,)
for idx in range(N):
	target = solutions[idx]
	elems = [
		elem
		for elem
		in solutions[:idx] + solutions[idx + 1:]
	]

	left, right, = 0, N - 2
	while left < right:
		conecentration = elems[left] + elems[right] + target
		if abs(conecentration) < abs(last_compare[0]):
			last_compare = (conecentration, target, elems[left], elems[right])
		if conecentration > 0:
			right -= 1
		else:
			left += 1
			
print(*last_compare[1:])
