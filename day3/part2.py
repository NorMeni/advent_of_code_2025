import os

with open('input.txt', 'r') as file:
	input = file.read().split('\n')
#input = input[:-1]
#input = ["1119811199111"]
#input = ["234234234234278"]
#input = ["811111111111119"]
#input = ["818181911112111"]

def int_to_array(num):
	return [int(d) for d in str(num)]

total = 0

max_limit = 11
current = 0
for bank in input:
	digits = int_to_array(bank)
	if len(digits) == 0: break
	#print(f"current bank: {digits}")
	length = len(digits)
	big_num = []
	subsect = []
	while len(big_num) < 12:
		end_index = (min(length, current + (length - max_limit) + 1) )
		if current >= end_index: break

		#create subsection
		subsect = digits[current:(length-max_limit)]

		biggest = 0
		for num in subsect:
			if num > biggest:
				biggest = num
		biggest_index = subsect.index(biggest)

		#print(f"subsect: {subsect}")

		big_num.append(biggest)
		current += biggest_index + 1
		max_limit -= 1
		subsect = []
		#print(f"new current: {current}\nnew max: {max_limit}")
	joltage = int(''.join(map(str, big_num)))
	total += joltage
	#print(f"big number: {big_num}\nadding: {joltage}")
	current = 0
	max_limit = 11
	big_num = []

print(f"Phew! Your total joltage is {total}!")
