import os

with open('input.txt', 'r') as file:
	input = file.read().split(',')

print(f"first id: {input[0]}")
ids = input[0].split('-')
print(f"both parts: {ids[0]} and {ids[1]}")


total = 0

for id in input:
	ranges = id.split('-')
	for i in range(int(ranges[0]), int(ranges[1])+1):
		if len(str(i)) % 2 == 1:
			continue
		else:
			s = str(i)
			mid = len(s) // 2
			first = int(s[mid:])
			second = int(s[:mid])
			if first == second:
				total += i

print(f"Hello sir! Your total is: {total}")
