cals = open('../input.txt', mode='r')
lines = cals.readlines()
calories = []
total = 0
top = 0

for line in lines:
        if line.strip():
            total += int(line)
        else:
            calories.append(total)
            total = 0

for i in range(3):
    top += max(calories)
    calories.remove(max(calories))

print(top)

cals.close()