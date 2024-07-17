s_len = int(input())

s = input()
count_2 = s.count('2')
count_e = s.count('e')

if count_2 == count_e:
	print('yee')
else:
	print('2' if count_2 > count_e else 'e')