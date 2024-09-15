import sys
readline = lambda : sys.stdin.readline().strip()
INF = sys.maxsize

N = int(readline())
solutions = list(map(int, readline().split()))


# ---- 투포인터 ----

# ans = (INF, -1, -1)

# left = 0
# right = N - 1
# while left < right:
#     s_l, s_r = solutions[left], solutions[right]
#     sum_ = s_l + s_r
#     if sum_ <= 0:
#         left += 1
#     else:
#         right -= 1
#     if abs(sum_) < abs(ans[0]):
#         ans = (sum_, s_l, s_r)

# print(*ans[1:])

# ---- 이분탐색 ----

ans = (INF, INF, INF)
for i in range(N - 1):
    current = solutions[i]
    left, right = i + 1, N - 1
    while left <= right:
        mid = (left + right) // 2
        if abs(current + solutions[mid]) < ans[0]:
            ans = (abs(current + solutions[mid]), current, solutions[mid])
        if solutions[mid] > -current:
            right = mid - 1
        else:
            left = mid + 1

ans = list(ans[1:])
print(*sorted(ans))