word_koo = sorted(input())
N = len(word_koo)
word_cube = sorted(input(), reverse=True)

res = ['?' for _ in range(N)]
index_res_front = 0
index_res_last = N - 1

turn_koo = True
index_koo_front = 0
index_koo_last = (N + 1) // 2 - 1
index_cube_front = 0
index_cube_last = N // 2 - 1

while index_res_front <= index_res_last:
	"""
	`<=` 대신 `<`를 사용하는 이유:

	cube의 경우 뒤에다 넣기 시작해 koo가 큰 문자를 앞에 넣도록 유도하는 것이 유리.
	koo의 경우 뒤에다 넣기 시작해도 손해 볼 것이 없음.

	따라서 그리디 관점에서, `<`로 비교해 확실하게 koo가 우위에 있을 때에만
	앞에다 채우는 것이 유리함
	"""
	if word_koo[index_koo_front] < word_cube[index_cube_front]:
		pos = index_res_front
		index_res_front += 1
		if turn_koo:
			word = word_koo[index_koo_front]
			index_koo_front += 1
		else:
			word = word_cube[index_cube_front]
			index_cube_front += 1
	else:
		pos = index_res_last
		index_res_last -= 1
		if turn_koo:
			word = word_koo[index_koo_last]
			index_koo_last -= 1
		else:
			word = word_cube[index_cube_last]
			index_cube_last -= 1

	res[pos] = word
	turn_koo = not turn_koo

print(''.join(res))