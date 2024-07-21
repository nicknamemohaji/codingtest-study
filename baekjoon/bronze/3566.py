"""
구현 문제. 브루트포스 느낌이긴 한데 별도의 방법이 없으니 이게 맞다 ㅇㅇ

math.ceil을 이용하면 효과적으로 계산할 수 있다.

"""
from math import ceil

r_h, r_v, s_h, s_v = map(int, input().split())

n = int(input())
monitors = list()
for _ in range(n):
	r_h_i, r_v_i, s_h_i, s_v_i, p_i  = map(int, input().split())
	monitors.append((r_h_i, r_v_i, s_h_i, s_v_i, p_i, ))

prices = list()
for r_h_i, r_v_i, s_h_i, s_v_i, p_i in monitors:
	require_h_h = max(ceil(r_h / r_h_i), ceil(s_h / s_h_i))
	require_v_h = max(ceil(r_v / r_v_i), ceil(s_v / s_v_i))
	require_h_v = max(ceil(r_h / r_v_i), ceil(s_h / s_v_i))
	require_v_v = max(ceil(r_v / r_h_i), ceil(s_v / s_h_i))
	
	price = min(
		require_h_h * require_v_h * p_i, 
		require_h_v * require_v_v * p_i, 
	)
	prices.append(price)

print(min(prices))