import os

with open('input.txt', 'r') as f:
	matrix = [list(line.strip()) for line in f if line.strip()]

#print(matrix)
#matrix = [['.', '.', '@', '@', '.', '@', '@', '@', '@', '.'], ['@','@','@','.','@','.','@','.','@','@']]
border = len(matrix[0]) - 1

def find_eight(row, col, border_right, border_bottom):
	coordinates = []

	#top
	if row - 1 >= 0:
		if col - 1 >= 0:
			coordinates.append( ((row-1), (col-1)) )
		coordinates.append( ((row-1), (col)) )
		if col + 1 < border_right:
			coordinates.append( ((row-1), (col+1)) )

	#left/right
	if col - 1 >= 0:
		coordinates.append( ((row), (col-1)) )
	if col + 1 < border_right:
		coordinates.append( ((row), (col+1)) )

	#bottom
	if row + 1 < border_bottom:
		if col - 1 >= 0:
			coordinates.append( ((row+1), (col-1)) )
		coordinates.append( ((row+1), (col)) )
		if col + 1 < border_right:
			coordinates.append( ((row+1), (col+1)) )

	return coordinates


def is_valid_tile(coordinates, matrix):
	count = 0
	for i in range(0, len(coordinates)):
		row = coordinates[i][0]
		col = coordinates[i][1]
		#print(f"checking ({row}, {col})")
		if matrix[row][col] == '@' or matrix[row][col] == 'X':
			#print(f"paper roll found at ({row}, {col})")
			count += 1
		if count == 4:
			return False
	return True

coordinates = []
total = 0

for row in range(0, len(matrix)):
	for col in range(0, len(matrix[0])):
		if matrix[row][col] == '@':
			coordinates = find_eight(row, col, len(matrix[0]), len(matrix))
			#print(f"coordinates for: ({row}, {col})\n{coordinates}")
			if is_valid_tile(coordinates, matrix):
				#print(f"can access tile ({row}, {col})")
				total += 1
				matrix[row][col] = 'X'
			coordinates = []

print(f"Total # of paper rolls demolished: {total}")
#print(f"final matrix:\n{matrix}")









