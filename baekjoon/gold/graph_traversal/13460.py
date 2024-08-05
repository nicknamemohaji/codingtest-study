N, M = map(int, input().split())
board = list()
for _ in range(N):
	board.append([c for c in input()])

def move_ball(board_copy: list, iter_: range, fixed_pos: int, b: str, vertical: bool) -> bool | tuple:
	for iter_pos in iter_:
		if vertical:
			check_pos = (iter_pos, fixed_pos)
		else:
			check_pos = (fixed_pos, iter_pos)
		if board_copy[check_pos[0]][check_pos[1]] == '.':
			last_pos = check_pos
			continue
		if board_copy[check_pos[0]][check_pos[1]] == 'O':
			return True
		board_copy[last_pos[0]][last_pos[1]] = b
		return last_pos

def move_board(board_copy: list, direction: str) -> bool | list:
	red_pos = None
	blue_pos = None
	for y in range(1, N - 1):
		for x in range(1, M - 1):
			if board_copy[y][x] == 'B':
				blue_pos = (y, x)
				board_copy[y][x] = '.'
			elif board_copy[y][x] == 'R':
				red_pos = (y, x)
				board_copy[y][x] = '.'
		if blue_pos and red_pos:
			break
	
	if direction == 'U':
		ball1 = (range(blue_pos[0], -1, -1), blue_pos[1], 'B', True)
		ball2 = (range(red_pos[0], -1, -1), red_pos[1], 'R', True)

		if blue_pos[0] > red_pos[0]:
			ball1, ball2, = ball2, ball1
		
	elif direction == 'D':
		ball1 = (range(blue_pos[0], N + 1, 1), blue_pos[1], 'B', True)
		ball2 = (range(red_pos[0],N + 1, 1), red_pos[1], 'R', True)

		if blue_pos[0] < red_pos[0]:
			ball1, ball2, = ball2, ball1
	
	elif direction == 'L':
		ball1 = (range(blue_pos[1], -1, -1), blue_pos[0], 'B', False)
		ball2 = (range(red_pos[1], -1, -1), red_pos[0], 'R', False)

		if blue_pos[1] > red_pos[1]:
			ball1, ball2, = ball2, ball1
		
	else:
		ball1 = (range(blue_pos[1], M + 1, 1), blue_pos[0], 'B', False)
		ball2 = (range(red_pos[1], M + 1, 1), red_pos[0], 'R', False)

		if blue_pos[1] < red_pos[1]:
			ball1, ball2, = ball2, ball1
	
	res1 = move_ball(board_copy, *ball1)
	res2 = move_ball(board_copy, *ball2)
	if res1 is True or res2 is True:
		return (res1 and ball1[2] == 'R' and res2 is not True) \
		 or (res2 and ball2[2] == 'R' and res1 is not True)
	if (ball1[2] == 'R' and res1 == red_pos and res2 == blue_pos) \
		or (ball2[2] == 'R' and res2 == red_pos and res2 == blue_pos):
		return False
	return board_copy

copy_board = lambda target: [li.copy() for li in target]

min_movement = 11

def dfs(direction, moves, board_copy):
	global min_movement

	moves += 1
	if moves >= min_movement:
		return
	res = move_board(board_copy, direction)
	if type(res) is bool:
		if res and min_movement > moves:
			min_movement = moves
		return
	for direction in 'UDLR':
		dfs(direction, moves, copy_board(res))

for direction in 'UDLR':
	dfs(direction, 0, copy_board(board))

print(min_movement if min_movement <= 10 else -1)
