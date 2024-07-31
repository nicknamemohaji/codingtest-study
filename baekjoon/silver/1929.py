M, N = map(int, input().split())

li = [True for _ in range((N + 1) + 1)]
li[1] = False
for i in range(2, N + 1):
	if not li[i]:
		continue
	multiple = i + i
	while multiple <= N + 1:
		li[multiple] = False
		multiple += i

for i in range(M, N + 1):
	if li[i]:
		print(i)
