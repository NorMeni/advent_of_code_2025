with open('input.txt', 'r') as file:
	content = file.read()

result = [tuple(map(int, line.split(','))) for line in content.strip().split('\n')]

#print(result)


def area(x1, y1, x2, y2):
	width = abs(x2 - x1) + 1
	height = abs(y2 - y1) + 1
	return width * height

largest = 0
current = 0
for i in range(0, len(result)):
	for j in range(i+1, len(result)):
		current = area(result[i][0], result[i][1], result[j][0], result[j][1])
		if current > largest:
			largest = current
		current = 0

print(f"larget area: {largest}")
