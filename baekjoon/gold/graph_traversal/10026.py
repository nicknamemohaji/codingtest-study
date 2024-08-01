import sys
from collections import deque
readline = sys.stdin.readline

N = int(readline().strip())
image = list()
for _ in range(N):
	image.append(readline().strip())

def findarea(colorblind: bool) -> int:
	global image
	vec = list([False] * N for _ in range(N))
	
	groups = 0
	while not all(all(vec[y][x] for x in range(N)) for y in range(N)):
		# 첫 그룹을 찾는다
		groups += 1
		queue = deque()
		for y in range(N):
			for x in range(N):
				if vec[y][x]:
					continue
				queue.append((y, x))
				break
			if queue:
				break
		vec[y][x] = True
		color = image[y][x]

		# bfs
		while queue:
			y, x = queue.popleft()
			for y, x in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
				if y < 0 or y == N or x < 0 or x == N:
					continue
				if vec[y][x]:
					continue
				if color != image[y][x]:
					if not (colorblind and color != 'B' and image[y][x] != 'B'):
						continue
				vec[y][x] = True
				queue.append((y, x))
	
	return groups

print(findarea(False), findarea(True))
