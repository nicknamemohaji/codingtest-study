N = int(input())

def is_hansu(n: int) -> bool:
	s = [int(c) for c in str(n)]
	return all([s[i - 1] - s[i - 2] == s[i] - s[i - 1] for i in range(2, len(s))])

count = 0
for n in range(1, N + 1):
	count += is_hansu(n)
print(count)