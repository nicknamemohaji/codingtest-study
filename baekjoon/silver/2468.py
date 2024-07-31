# 큐를 사용하기 위해 앞에서 꺼낼 수 있는 deque 컨테이너 사용
from collections import deque

N = int(input())
areas = list()
for y in range(N):
	line = [int(n) for n in input().split()]
	areas.extend([(y, x, height) for x, height, in zip(range(N), line)])

def count_groups(rain: int) -> int:
	global areas, N
	area_vec = [[0] * N for _ in range(N)]

	while areas:
		y, x, height = areas.pop()
		area_vec[y][x] = 0 if height <= rain else height
	
	queue = deque()
	ret = 0
	while True:
		# 탐색을 시작할 칸을 찾는다
		for y in range(N):
			for x in range(N):
				if not area_vec[y][x]:
					continue
				queue.append((y, x, area_vec[y][x]))
				area_vec[y][x] = False
				break
			if queue:
				break
		# 탐색의 종료조건
		if not queue:
			break
		# 적어도 하나의 그룹을 추가로 만들 수 있다
		ret += 1

		# 인접한 모든 영역에 대해 bfs
		while queue:
			y, x, height, = queue.popleft()
			areas.append((y, x, height))
			for _y, _x in ((y-1,x), (y+1,x), (y,x-1), (y,x+1)):
				if _y < 0 or _y == N or _x < 0 or _x == N:
					continue
				if not area_vec[_y][_x]:
					continue
				
				queue.append((_y, _x, area_vec[_y][_x]))
				area_vec[_y][_x] = False
	
	del area_vec
	return ret

max_groups = 0
for i in range(0, 101):
	group = count_groups(i)
	if group == 0:
		break
	if max_groups < group:
		max_groups = group
print(max_groups)