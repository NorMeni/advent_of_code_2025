import os

directions = []

with open('input.txt', 'r') as file:
        for line in file:
                directions.append(line[:-1])
        file.close()

print(directions)


current = 50
password = 0

for step in directions:
        number = int(step[1:])
        password += int(number/100)
        number %= 100
        if step[0] == 'L':
                previous = current
                current -= number
                if current == 0:
                        password += 1
                        continue
                elif current < 0:
                        if previous == 0:
                                current += 100
                                continue
                        current += 100
                        password += 1
                        continue
        elif step[0] == 'R':
                current += number
                if current == 100:
                        password += 1
                        current = 0
                        continue
                elif current > 100:
                        current -= 100
                        password += 1
                        continue

print(f"Ta-da! Your password is: {password}")
