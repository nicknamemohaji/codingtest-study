"""
O(N), 투포인터 풀이
"""
import sys
readline = sys.stdin.readline

N, S, = map(int, readline().strip().split())
numbers = list(map(int, readline().strip().split()))

slow_ptr, fast_ptr, = 0, 0
partial_sum = 0
least_range = N + 1
move_fast = True

while slow_ptr <= N and fast_ptr <= N:
	if move_fast and fast_ptr == N:
		break
	if not move_fast and slow_ptr == N:
		break
	if move_fast:
		partial_sum += numbers[fast_ptr]
		fast_ptr += 1
		if partial_sum >= S:
			least_range = min(least_range, fast_ptr - slow_ptr)
			move_fast = False
	else:
		partial_sum -= numbers[slow_ptr]
		slow_ptr += 1
		if partial_sum >= S:
			least_range = min(least_range, fast_ptr - slow_ptr)
		else:
			move_fast = True

print(least_range if least_range < N + 1 else 0)
