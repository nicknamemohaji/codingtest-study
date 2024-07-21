"""
# 풀이

그리디, 가장 작은 카드뭉치를 만들어라, 합친 카드뭉치는 계속 더해지기 떄문
(10 + 20) + ((10 + 20) + 40) + ...

"""

from heapq import heappush, heappop, heapify

N = int(input())
cards = list()
for _ in range(N):
	cards.append(int(input()))

heapify(cards)
compare_cnt = 0
while len(cards) > 1:
	c1 = heappop(cards)
	c2 = heappop(cards)

	compare_cnt += c1 + c2
	heappush(cards, c1 + c2)

print(compare_cnt)
