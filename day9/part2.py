with open('input.txt', 'r') as file:
    content = file.read()

points = [tuple(map(int, line.split(','))) for line in content.strip().split('\n')]

edges = []
for i in range(len(points)):
	p1 = points[i]
	p2 = points[(i + 1) % len(points)]
	edges.append((p1, p2))

def get_area(x1, y1, x2, y2):
    width = abs(x2 - x1) + 1
    height = abs(y2 - y1) + 1
    return width * height


def point_inside(tx, ty):
	crossings = 0
	n = len(points)
	for i in range(n):
		x1, y1 = points[i]
		x2, y2 = points[(i+1) % n]
		if x1 == x2 and x1 > tx:
			if min(y1, y2) < ty < max(y1, y2):
				crossings += 1
	return crossings % 2 == 1

def edge_cuts_through(edge, rect):
	(x1, y1), (x2, y2) = rect
	(ex1, ey1), (ex2, ey2) = edge

	if ex1 == ex2:
		xe = ex1
		ye_min = min(ey1, ey2)
		ye_max = max(ey1, ey2)
		if x1 < xe < x2:
			return not (ye_max <= y1 or ye_min >= y2)

	elif ey1 == ey2:
		ye = ey1
		xe_min = min(ex1, ex2)
		xe_max = max(ex1, ex2)
		if y1 < ye < y2:
			return not (xe_max <= x1 or xe_min >= x2)

	return False


largest = 0
for i in range(len(points)):
	for j in range((i+1), len(points)):
		x1, y1 = points[i]
		x2, y2 = points[j]
		xl, xr = sorted([x1, x2])
		yb, yt = sorted([y1, y2])
		area = get_area(x1, y1, x2, y2)

		if area <= largest:
			continue
		if not point_inside(xl + 0.5, yb + 0.5):
			continue
		rect = ((xl, yb), (xr, yt))
		if any(edge_cuts_through(edge, rect) for edge in edges):
			continue

		largest = area
		best_corners = (points[i], points[j])


print(f"largest area is {largest}\ndiagonal corners: {best_corners}")
