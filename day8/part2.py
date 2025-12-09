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
	return x_pow + y_pow + z_pow

def all_pairs(coords):
	pairs = []
	for i in range(len(coords)):
		for j in range(i+1, len(coords)):
			dist_sq = calculate_distance(coords[i][0], coords[i][1], coords[i][2], coords[j][0], coords[j][1], coords[j][2])
			pairs.append((dist_sq, coords[i], coords[j]))
	pairs.sort(key=lambda x: x[0])
	return pairs

def find(parent, box):
	while parent[box] != box:
		parent[box] = parent[parent[box]]
		box = parent[box]
	return box

def union(parent, box1, box2):
	root1 = find(parent, box1)
	root2 = find(parent, box2)
	if root1 != root2:
		parent[root2] = root1
		return True
	return False



pairs = all_pairs(coordinates)

parent = {box: box for box in coordinates}
num_circuits = len(coordinates)
last_pair = None


for dist, box1, box2 in pairs:
	if find(parent, box1) != find(parent, box2):
		union(parent, box1, box2)
		num_circuits -= 1
		last_pair = (box1, box2)
		if num_circuits == 1:
			break

answer = last_pair[0][0] * last_pair[1][0]
print(f"final answer.... {answer}")




