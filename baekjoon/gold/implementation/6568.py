while True:
	# in bytes
	memory = [0] * 32

	try:
		memory[0] = input()
	except EOFError:
		break
	PC = 1
	while PC < 32:
		memory[PC] = input()
		PC += 1

	# initial status
	adder = 0
	PC = 0

	while True:
		line = memory[PC]
		comm, operand, = (int(line[:3], 2), int(line[3:], 2))
		PC += 1
		if PC > 0x1f:
			PC = 0x00
		
		# STA x
		if comm == 0:
			memory[operand] = f"{adder:08b}"
		# LDA x
		elif comm == 1:
			adder = int(memory[operand], 2)
		# BEQ x
		elif comm == 2:
			if adder == 0:
				PC = operand
		# NOP
		elif comm == 3:
			pass
		# DEC
		elif comm == 4:
			adder -= 1
			if adder < 0:
				adder = 0xff
		# INC
		elif comm == 5:
			adder += 1
			if adder > 0xff:
				adder = 0x00
		# JMP x
		elif comm == 6:
			PC = operand
		# HLT
		else:
			break

	print(f"{adder:08b}")