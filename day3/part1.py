import os

with open('input.txt', 'r') as file:
	input = file.read().split('\n')
#input = input[:-1]
#input = ["4453322423234323362634238645943333332463321659433346534324232461344544333233244323632243313334262243"]
def int_to_array(num):
	return [int(d) for d in str(num)]

total = 0

for bank in input:
	if len(bank) == 0: break
	digits = int_to_array(bank)
	first = digits[0]
	second = 0

	tens = 1
	ones = digits[len(digits)-1]
	best = 0
	#print(f"current bank: {bank}")
	for num in reversed(range(len(digits)-1)):
		if digits[num] >= tens:
			if digits[num] > ones and tens > ones:
				ones = tens
				tens = digits[num]
			tens = digits[num]
		voltage = (tens * 10) + ones
		if voltage > best:
			best = voltage
		#print(f"digit {digits[num]}\nvoltage: {voltage}\nbest: {best}")
	total += best


print(f"Zap! Your final voltage is {total}!")
