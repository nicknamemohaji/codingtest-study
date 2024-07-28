import sys
from collections import deque

MAX = 1 << 31

R, C = map(int, sys.stdin.readline().rstrip().split())
blocks = list()
for _ in range(R):
	blocks.append([(0 if n == '0' else MAX) for n in sys.stdin.readline().rstrip().split()])
N = int(sys.stdin.readline().rstrip())
movements = list()
for _ in range(N):
	movements.append([int(n) for n in sys.stdin.readline().rstrip().split()])

costs = set()
queue = deque([(x, 0, 0) for x in range(C) if blocks[0][x] != 0])
while queue:
	posx, posy, cost, = queue.popleft()
	if posy == R - 1:
		costs.add(cost)
		continue
	
	cost += 1
	new_pos = list()
	for rx, cx, in movements:
		nexty, nextx = (posy + rx), (posx + cx)
		if not (0 <= nextx < C and 0 <= nexty < R and 0 < cost < blocks[nexty][nextx]):
			continue
		blocks[nexty][nextx] = cost
		new_pos.append((nextx, nexty, cost))
	queue.extend(new_pos)

try:
	print(min(costs))
except ValueError:
	print(-1)
