import sys
readline = sys.stdin.readline

n = int(readline().strip())
nums = list(map(int, readline().strip().split()))
nums.sort()
x = int(readline().strip())

left = 0
right = n - 1
count = 0

while left < right:
	num_left = nums[left]
	num_right = nums[right]
	num_sum = num_left + num_right

	if num_sum < x:
		left += 1
		continue
	elif num_sum > x:
		right -= 1
		continue
	count += 1
	if num_left == nums[left + 1]:
		left += 1
	else:
		right -= 1

print(count)
"""
도갓: 투포인터는 포인터를 움직였을 때 다음 상태가 어떻게 되든 상관없어야 한다.
왼쪽 포인터를 움직였다면 그 왼쪽 상태는 다시 확인할 필요가 없어야 
O(N ** 2)를 O(N)으로 최적화할 수 있게 되는 것이다.

정렬을 한 후에 투포인터를 쓰는 이유가 그거다 - 
a + b < x라면 그보다 작은 수는 더 이상 볼 필요가 없으니 왼쪽 포인터를 움직이면 된다.

생각할 것:
- 투포인터의 본질: 알고리즘이 아님. O(N)으로 만드는 최적화 기법
- 투포인터 상황: 이전 상황과 다음 상황이 명확한 상황

주의할 점: 
- a + b == x일 때 왼쪽과 오른쪽 중 어느 것을 움직일 것인가
- 조건상 중복되는 수가 있을 수 있는데 어떻게 처리할 것인가
"""