T = int(input())

for i in range(T):
	R, S = input().split(' ')
	R = int(R)
	print(''.join([c * R for c in S]))
