with open('input.txt', 'r') as file:
	content = file.read()

matrix = []

for line in content.split('\n'):
	matrix.append(line)

matrix = matrix[:-1]

#print(matrix)

starting_point = 0
for i in range(0, len(matrix[0])):
	if matrix[0][i] == 'S':
		starting_point = i

points = [starting_point]
total = 0
remove_values = []
splits = 0
found = []

print(f"points: {points}")
for row in range(1, len(matrix)):
	print(f"currently on row: {row}\n{matrix[row]}")
	points.sort()
	points = [x for x in points if x not in remove_values]
	remove_values = []
	for point in points:
		if matrix[row][point] == '.':
			continue
		if matrix[row][point] == '^':
			remove_values.append(point)
			splits += 1
			found.append(point)
			if (0 <= point - 1 <= len(matrix[0])) and (point-1) not in points:
				points.append(point-1)
			if (0 <= point + 1 <= len(matrix[0])) and (point+1) not in points:
				points.append(point+1)
	#if splits == 0:
		#points = new_points
	print(f"found points at {found}\nsplitting at {points}\nsplit {splits} times")
	total += splits
	splits = 0
	found = []

print(f"total # of splits: {total}")
