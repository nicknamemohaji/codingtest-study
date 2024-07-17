import math

inputs: list[str] = []
for _ in range(5):
	inputs.append(input())

L, A, B, C, D = map(int, inputs)

print(L - max(math.ceil(A / C), math.ceil(B / D)))