with open('input.txt', 'r') as file:
	content = file.read()

coordinates = []

for line in content.split('\n'):
	coordinates.append(line)
coordinates = coordinates[:-1]

coordinates = [tuple(map(int, s.split(','))) for s in coordinates]

#print(coordinates)

def calculate_distance(x1, y1, z1, x2, y2, z2):
	x_pow = (x2 - x1)*(x2 - x1)
	y_pow = (y2 - y1)*(y2 - y1)
	z_pow = (z2 - z1)*(z2 - z1)
	total = x_pow + y_pow + z_pow
	return total ** (1/2)

def create_smallest_list(coords):
	shortest_list = [float('inf')] * 1000
	coord_list = [] * 1000
	for i in range(0, len(coords)):
		x1, y1, z1 = coords[i][0], coords[i][1], coords[i][2]
		for j in range(i+1, len(coords)):
			x2, y2, z2 = coords[j][0], coords[j][1], coords[j][2]
			distance = calculate_distance(x1, y1, z1, x2, y2, z2)
			if distance < shortest_list[-1]:
				for num in range(0, len(shortest_list)):
					if distance < shortest_list[num]:
						shortest_list = shortest_list[:num] + [distance] + shortest_list[num:-1]
						coord_list = coord_list[:num] + [(coords[i], coords[j])] + coord_list[num:-1]
						break
	return coord_list, shortest_list

def create_dict(smallest_list):
	circuit_dict = {}
	circuit_id = 0
	for box1, box2 in smallest_list:
		id1 = circuit_dict.get(box1)
		id2 = circuit_dict.get(box2)

		if id1 is None and id2 is None:
			circuit_dict[box1] = circuit_id
			circuit_dict[box2] = circuit_id
			circuit_id += 1
		elif id1 is not None and id2 is not None:
			if id1 != id2:
				for box in circuit_dict.keys():
					if circuit_dict[box] == id2:
						circuit_dict[box] = id1
		else:
			existing_id = id1 if id1 is not None else id2
			circuit_dict[box1] = existing_id
			circuit_dict[box2] = existing_id

	return circuit_dict

def product_top_three(circuit_dict):
	counts = {}
	for circuit_id in circuit_dict.values():
		counts[circuit_id] = counts.get(circuit_id, 0) + 1
	count_list = []
	for val in counts.values():
		count_list.append(val)

	for i in range(len(count_list)):
		for j in range(i+1, len(count_list)):
			if count_list[i] < count_list[j]:
				count_list[i], count_list[j] = count_list[j], count_list[i]

	product = 1
	for i in range(min(3, len(count_list))):
		product *= count_list[i]

	return product

list, short_list = create_smallest_list(coordinates)
print(f"new list:\n{list}\nand distances:\n{short_list}")
circuit_dict = create_dict(list)
print(f"dictionary:\n{circuit_dict}")
total = product_top_three(circuit_dict)
print(f"total circuits or whatever: {total}")





#[(162, 817, 812), (57, 618, 57), (906, 360, 560), (592, 479, 940), (352, 342, 300), (466, 668, 158), (542, 29, 236), (431, 825, 988), (739, 650, 466), (52, 470, 668), (216, 146, 977), (819, 987, 18), (117, 168, 530), (805, 96, 715), (346, 949, 466), (970, 615, 88), (941, 993, 340), (862, 61, 35), (984, 92, 344), (425, 690, 689)]
