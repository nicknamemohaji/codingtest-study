import sys

X, Y, = map(int, input().split())

min_val = 1
max_val = 99 * X - 100 * Y
if max_val <= 0:
	print(-1)
	sys.exit(0)

curr_rate = int(Y * 100 / X)

def parametric_search(left, right):
	if left == right:
		return left
	
	global X, Y, curr_rate
	mid = (left + right) // 2
	
	new_rate = int((Y + mid) * 100 / (X + mid))
	if new_rate != curr_rate:
		right = mid
	else:
		left = mid + 1
	return parametric_search(left, right)

print(parametric_search(min_val, max_val))