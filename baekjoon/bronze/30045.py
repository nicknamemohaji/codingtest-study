import re

N = int(input())

count = 0
r = re.compile(r'(01)|(OI)')
for i in range(N):
	S = input()
	count += 1 if len(r.findall(S)) != 0 else 0

print(count)