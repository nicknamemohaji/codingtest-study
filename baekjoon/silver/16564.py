import sys
readline = sys.stdin.readline

def find_index(target):
	global characters, N
	left, right, = 0, N

	while left < right:
		mid = (left + right) // 2
		if characters[mid] > mid_level:
			right = mid
		else:
			left = mid + 1
	return left

N, K = map(int, readline().strip().split())
characters = list()
for _ in range(N):
	characters.append(int(readline().strip()))
characters.sort()

min_level = 0
max_level = 1000000000 * 2
while min_level < max_level:
	mid_level = (min_level + max_level + 1) // 2
	idx = find_index(mid_level)
	cost = sum(mid_level - character for character in characters[:idx])

	if cost > K:
		max_level = mid_level - 1
	else:
		min_level = mid_level

print(min_level)