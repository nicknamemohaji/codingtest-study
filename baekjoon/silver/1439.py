s = [int(c) for c in input()]

count_group = [0, 0]

flag = s[0]
for c in s:
	if flag != c:
		count_group[flag] += 1
		flag = c

count_group[flag] += 1
print(min(count_group))