import bisect

import sys
readline = sys.stdin.readline
N = int(input())
nums = list(map(int, readline().strip().split()))

largest_sequences = [[nums[0], 1]]
llen = 1
for n in nums[1:]:
	search = bisect.bisect_left(largest_sequences, n, key=lambda s: s[0])
	if search >= llen:
		if largest_sequences[-1][0] == n:
			continue
		largest_sequences.append([n, largest_sequences[-1][1] + 1])
		llen += 1
	else:
		if largest_sequences[search][0] > n:
			largest_sequences[search][0] = n

print(largest_sequences[-1][1])