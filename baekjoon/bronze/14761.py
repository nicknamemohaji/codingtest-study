X, Y, N = map(int, input().split())

for i in range(1, N + 1):
	mod_X = i % X
	mod_Y = i % Y
	if mod_X == 0 and mod_Y == 0:
		print('FizzBuzz')
	elif mod_X == 0:
		print('Fizz')
	elif mod_Y == 0:
		print('Buzz')
	else:
		print(i)