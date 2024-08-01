import sys
from collections import deque
readline = sys.stdin.readline

# 입력
N, M, H = map(int, readline().strip().split())
tomatoes = list()
for _ in range(H):
	box = list()
	for _ in range(M):
		box.append(list(map(int, readline().strip().split())))
	tomatoes.append(box)

check = lambda li: not any(any(any(elem == 0 for elem in yline) for yline in zline) for zline in li)

# 큐에 익은 토마토 기록. 큐에 있는 익은 토마토를 기준으로 bfs 수행
# 저는감자입니다
queue = list()
for z in range(H):
	queue.extend([(z, y, x) for y in range(M) for x in range(N) if tomatoes[z][y][x] == 1])
queue = deque(queue)


# 1일씩 진행
days = 0
while queue and not check(tomatoes):
	days += 1
	new_queue = deque()
	while queue:
		z, y, x, = queue.popleft()
		for z, y, x in ((z + 1, y, x), (z - 1, y, x), (z, y + 1, x), (z, y - 1, x), (z, y, x + 1), (z, y, x - 1)):
			if z < 0 or z == H or y < 0 or y == M or x < 0 or x == N:
				continue
			if tomatoes[z][y][x] != 0:
				continue
			tomatoes[z][y][x] = 1
			new_queue.append((z, y, x))
	queue = new_queue

print(days if check(tomatoes) else -1)