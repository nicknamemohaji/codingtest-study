from collections import deque
import sys
INF = sys.maxsize
readline = lambda : sys.stdin.readline().strip()

N, K, = map(int, readline().split())

def addtoqueue(new_pos: int, cost: int, cost_diff: int) -> None:
    global costs, queue, ans
    new_cost = cost + cost_diff
    if new_pos < 0:
        return
    if new_cost >= ans:
        return
    if new_pos in costs and costs[new_pos] <= new_cost:
        return
    costs[new_pos] = new_cost
    if cost_diff == 1:
        queue.append((new_pos, new_cost))
    else:
        queue.appendleft((new_pos, new_cost))

costs = dict(N = 0)
ans = INF
queue = deque([(N, 0)])
while queue:
    pos, cost, = queue.popleft()
    if pos == K:
        ans = min(ans, cost)
        continue
    if pos in costs and costs[pos] < cost:
        continue
    if pos > K:
        addtoqueue(pos - 1, cost, 1)
        continue
    for new_pos, new_cost in (
        (pos - 1, 1),
        (pos + 1, 1),
        (pos * 2, 0)
        ):
        addtoqueue(new_pos, cost, new_cost)

print(ans)