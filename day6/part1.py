import re

with open('input.txt', 'r') as file:
	content = file.read()

matrix = []
for line in content.strip().split('\n'):
	row = [item for item in line.split() if item]
	matrix.append(row)
#print(matrix)
total = 0
for col in range(len(matrix[0])):
	addition = 0
	multiplication = 1
	operator = matrix[len(matrix)-1][col]
	for row in range(0, len(matrix)-1):
		if operator == '+':
			addition += int(matrix[row][col])
		else:
			multiplication *= int(matrix[row][col])
	if addition > 0:
		total += addition
	if multiplication > 1:
		total += multiplication

print(f"Your total: {total}")
