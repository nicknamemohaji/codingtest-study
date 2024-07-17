K, N = map(int, input().split())

lengths: list[int] = []
for i in range(K):
	lengths.append(int(input()))

lower_bound = 1
upper_bound = max(lengths)

while lower_bound < upper_bound:
	mid = (lower_bound + upper_bound + 1) // 2
	wires = sum([l // mid for l in lengths])

	if wires < N:
		upper_bound = mid - 1
	else:
		lower_bound = mid

print(lower_bound)
