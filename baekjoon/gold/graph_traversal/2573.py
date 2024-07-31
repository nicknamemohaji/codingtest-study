import sys
from collections import deque

readline = sys.stdin.readline

N, M = map(int, readline().strip().split())
maps = list()
for _ in range(N):
	maps.append([int(n) for n in readline().strip().split()])

def melt() -> bool:
	global maps, ices, N, M
	queue = list()
	for y in range(N):
		for x in range(M):
			if maps[y][x] == 0:
				continue
			new_val = maps[y][x] - (
				(maps[y - 1][x] == 0) + (maps[y + 1][x] == 0) + (maps[y][x - 1] == 0) + (maps[y][x + 1] == 0))
			queue.append((y, x, new_val))

	ret = False
	ices.clear()
	for y, x, new_val, in queue:
		if new_val > 0:
			ices.append((y, x))
			ret = True
		elif new_val < 0:
			new_val = 0
		maps[y][x] = new_val
	del queue
	return ret

ices = list()
def count_groups() -> bool:
	global ices, N, M
	ice_vec = [[False] * M for _ in range(N)]

	y: int
	x: int
	while ices:
		y, x, = ices.pop()
		ice_vec[y][x] = True
	ices.clear()
	
	queue = deque()
	queue.append((y,x,))
	ice_vec[y][x] = False
	while queue:
		y, x = queue.popleft()
		for _y, _x in ((y-1,x), (y+1,x), (y,x-1), (y,x+1)):		
			if ice_vec[_y][_x]:
				ice_vec[_y][_x] = False
				queue.append((_y, _x))
	
	ret = all([all([v == False for v in line]) for line in ice_vec])
	del ice_vec
	return ret


year = 0
while melt():
	year += 1
	if not count_groups():
		print(year)
		sys.exit(0)
print(0)