import sys
readline = lambda : sys.stdin.readline().strip()

M, N, = map(int, readline().split())

tomatoes = list()
for _ in range(N):
    tomatoes.append(list(map(int, readline().split())))

check_remainig = lambda li: any(any(elem == 0 for elem in yline) for yline in li)

days = 0
queue = [(y, x) for y in range(N) for x in range(M) if tomatoes[y][x] == 1]
while check_remainig(tomatoes) and queue:
    days += 1
    new_queue = list()
    while queue:
        _y, _x = queue.pop()
        for y, x, in (
                (_y + 1, _x), (_y - 1, _x), (_y, _x - 1), (_y, _x + 1)
            ):
            if y < 0 or y >= N or x < 0 or x >= M:
                continue
            if tomatoes[y][x] != 0:
                continue
            tomatoes[y][x] = 1
            new_queue.append((y, x,))
    queue = new_queue


print(days if not check_remainig(tomatoes) else -1)