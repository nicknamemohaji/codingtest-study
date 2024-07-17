N = int(input())

row = 1
while (row * row + row) // 2 < N:
	row += 1
col = N - (row * row - row) // 2
print(row - col + 1, col)