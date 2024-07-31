import heapq
import sys
readline = sys.stdin.readline

N = int(readline().strip())
nums = list()
for _ in range(N):
	nums.append(int(readline().strip()))
nums.sort()

avg = sum(nums) / N

middle = nums[N // 2]

_range = nums[-1] - nums[0]

last_num = nums[0]
last_occur = 1
occur_heap = [(0, False)]
for n in nums[1:]:
	if last_num == n:
		last_occur += 1
	else:
		heapq.heappush(occur_heap, (-last_occur, last_num))
		last_num = n
		last_occur = 1
heapq.heappush(occur_heap, (-last_occur, last_num))

print(int(round(avg, 0)))
print(middle)
most1 = heapq.heappop(occur_heap)
most2 = heapq.heappop(occur_heap)
if most1[0] < most2[0]:
	print(most1[1])
else:
	print(most2[1])
print(_range)
