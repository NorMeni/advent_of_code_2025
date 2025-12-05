with open('input.txt', 'r') as f:
	content = f.read().splitlines()


ranges = []
for line in content[:content.index('')]:
	start, end = map(int, line.strip().split('-'))
	ranges.append( (start, end) )

ranges.sort(key=lambda x: x[0])

merged = []
current_start, current_end = ranges[0]

for start, end in ranges[1:]:
	if start <= current_end + 1:
		current_end = max(current_end, end)
	else:
		merged.append((current_start, current_end))
		current_start, current_end = start, end


merged.append( (current_start, current_end) )

total_count = 0
for start, end in merged:
	total_count += (end - start + 1)

print(f"All fresh IDs: {total_count}")
