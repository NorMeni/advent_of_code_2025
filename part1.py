with open('input.txt', 'r') as f:
	content = f.read().splitlines()

id_list = [line.strip() for line in content[:content.index('')]]
ingredient_list = [int(line.strip())for line in content[content.index('') + 1:] if line.strip()]

#print(id_list)
#print(ingredient_list)


def is_fresh(ingredient, id_list):
	for i in range(0, len(id_list)):
		ranges = id_list[i].split('-')
		if ingredient >= int(ranges[0]) and ingredient <= int(ranges[1]):
			#print(f"ingredient {ingredient} is fresh! It falls between {ranges[0]} and {ranges[1]}")
			return True
	#print(f"ingredient {ingredient} is rotten!")
	return False

total = 0
for ingredient in ingredient_list:
	if is_fresh(ingredient, id_list):
		total += 1


print(f"Yummers! Total amount of fresh ingredients: {total}")
