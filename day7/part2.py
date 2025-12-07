with open('input.txt', 'r') as file:
	content = file.read()

matrix = []

for line in content.split('\n'):
	matrix.append(line)
matrix = matrix[:-1]

starting_point = 0
for i in range(0, len(matrix[0])):
	if matrix[0][i] == 'S':
		starting_point = i

depth = len(matrix)
print(f"depth is: {depth}")
total = 0

cache = {}
def find_timeline(row, col):
	key = (row, col)
	if key in cache:
		return cache[key]

	if col < 0 or col >= len(matrix[0]):
		cache[key] = 0
		return 0
	if row == depth - 1:
		cache[key] = 1
		return 1

	count = 0
	if matrix[row][col] == '.':
		count += find_timeline((row+1), col)
	if matrix[row][col] == '^':
		count += find_timeline((row+1), (col-1))
		count += find_timeline((row+1), (col+1))

	cache[key] = count
	return count

total = find_timeline(1, starting_point)

print(f"total timelines: {total}")
