N, M = map(int, input().split())
board = list()
for _ in range(N):
	board.append([True if piece == 'B' else False for piece in input()])

def bruteforce(selected_board: list, start: bool) -> int:
	paints = 0
	for y in range(8):
		start = not start
		paints += sum([(start := not start) == selected_board[y][x] for x in range(8)])
	return paints

min_paint = 8 * 8
for y in range(N - 8 + 1):
	for x in range(M - 8 + 1):
		selected_board = [board[_y][x : x+8] for _y in range(y, y + 8)]
		paint_black = bruteforce(selected_board, True)
		paint_white = 64 - paint_black
		min_paint = min(min_paint, paint_black, paint_white)

print(min_paint)