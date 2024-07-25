from bisect import bisect_right
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
ballons = list()
for _ in range(N):
	x, y, health = map(int, sys.stdin.readline().rstrip().split())
	ballons.append((x, y, health,))

ballons.sort(key=lambda x: x[2])
px, py, _ = ballons[0]

total_damage = 0
for _ in range(M):
	ax, ay, damage = map(int, sys.stdin.readline().rstrip().split())

	attack_success = (ay * px == ax * py)
	attack_success &= ((ay > 0 and py > 0) or (ay < 0 and py < 0) or (ay == py))
	attack_success &= ((ax > 0 and px > 0) or (ax < 0 and px < 0) or (ax == px))

	if attack_success:
		total_damage += damage
	
	print(N - bisect_right(ballons, total_damage, key=lambda x: x[2]))
