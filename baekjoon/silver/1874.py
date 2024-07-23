from collections import deque

n = int(input())
target = list()
for _ in range(n):
	target.append(int(input()))

li = deque([num for num in range(1, n + 1)])
new_li = list()
stack = list()

operataions = list()
target_index = 0
while li:
	if stack and stack[-1] == target[target_index]:
		operataions.append('-')
		new_li.append(stack.pop())
		target_index += 1
	else:
		operataions.append('+')
		stack.append(li.popleft())
while stack:
	operataions.append('-')
	new_li.append(stack.pop())

if new_li == target:
	for op in operataions:
		print(op)
else:
	print('NO')