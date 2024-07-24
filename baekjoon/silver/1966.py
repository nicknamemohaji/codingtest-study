from collections import deque

tc_count = int(input())

for _ in range(tc_count):
	N, M = map(int, input().split())
	li = map(int, input().split())

	li = deque(li)
	count = 0
	while True:
		if li[0] >= max(li):
			count += 1
			if M == 0:
				print(count)
				break
			else:
				li.popleft()
				M = M - 1
		else:
			M = M - 1
			if M < 0:
				M = len(li) - 1
			li.append(li.popleft())

