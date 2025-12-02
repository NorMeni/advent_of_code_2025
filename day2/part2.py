import os

with open('input.txt', 'r') as file:
	input = file.read().split(',')
print(f"{input}")

#input = ["824824824-824824825"]

total = 0

def isValidID(id):
	length = len(id)
	for patternLen in range(1, length//2 + 1):
		if length % patternLen != 0: continue

		pattern = id[:patternLen]
		valid = True

		for i in range(patternLen, length, patternLen):
			if id[i:i+patternLen] != pattern:
				valid = False
				break
		if valid: return True
	return False

for id in input:
	ranges = id.split('-')
	#print(f"ranges from {ranges[0]} to {ranges[1]}")

	#num-num
	for i in range(int(ranges[0]), int(ranges[1])+1):
		if isValidID(str(i)):
			total += i

print(f"Phew! That was a lot of work! Your total is: {total}")

