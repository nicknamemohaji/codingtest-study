inputs = list()
for i in range(3):
	inputs.append(input())

s1, s2, s3, = inputs
n: int
if (s1.isnumeric()):
	n = int(s1) + 3
elif (s2.isnumeric()):
	n = int(s2) + 2
else:
	n = int(s3) + 1

mod_3 = n % 3
mod_5 = n % 5
if mod_3 == 0 and mod_5 == 0:
	print('FizzBuzz')
elif mod_3 == 0:
	print('Fizz')
elif mod_5 == 0:
	print('Buzz')
else:
	print(n)