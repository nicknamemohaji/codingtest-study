from collections import deque

N, K = map(int, input().split())

circle = deque(range(N))
execution = list()

while circle:
	for i in range(K - 1):
		circle.append(circle.popleft())
	execution.append(str(circle.popleft() + 1))

print(f"<{', '.join(execution)}>")