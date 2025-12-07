import re

with open('input.txt', 'r') as file:
	matrix = file.read().splitlines(keepends=True)
	matrix = [line[:-1] if line.endswith('\n') else line for line in matrix]
print(matrix)

numbers = []
total = 0
for col in range(len(matrix[0])-1, -1, -1):
	#print(f"current col: {col}")
	digits = []
	add = False
	multiply = False
	for row in matrix:
		#print(f"current row: {row}")
		#print(f"row[col]: {row[col]}")
		match row[col]:
			case ' ':
				continue
			case '+':
				add = True
			case '*':
				multiply = True
			case _:
				digits.append(row[col])

	if len(digits) > 0:
		numbers.append(int(''.join(map(str, digits))))
	digits = []
	#print(f"current numbers list: {numbers}")
	if add:
		add = False
		total += sum(numbers)
		numbers = []
	if multiply:
		multiply = False
		product = 1
		for num in numbers:
			product *= num
		total += product
		numbers = []

print(f"Total: {total}")
