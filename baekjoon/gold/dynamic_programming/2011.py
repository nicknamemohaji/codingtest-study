from typing import Literal
import sys
sys.setrecursionlimit(10000)

mod = 1000000
code = [int(c) for c in input()]
code_len = len(code)
cases = [-1] * code_len

def find(pos: int) -> int:
	global code, cases, code_len
	if pos >= code_len:
		return 0
	if pos + 1 == code_len:
		cases[pos] = 1
		return 1
	if cases[pos] != -1:
		return cases[pos]
	
	step_1 = 0
	step_2 = 0
	if code[pos + 1] in range(1, 10):
		step_1 = find(pos + 1)
	if pos + 2 < code_len and 10 <= (code[pos + 1]  * 10 + code[pos + 2]) <= 26:
		step_2 = find(pos + 2)
	if pos == -1:
		return (step_1 + step_2) % mod
	cases[pos] = (step_1 + step_2) % mod
	return cases[pos]

print(find(-1))
