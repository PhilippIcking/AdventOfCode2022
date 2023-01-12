with open("input09.txt") as f:
    inp = f.read().splitlines()

commands = []
for x in inp:
    direct, cou = x.split()
    commands.append((direct, int(cou)))

com_dic = {
    "L": (-1, 0),
    "R": (1, 0),
    "U": (0, -1),
    "D": (0, 1)
}
positions = [[500, 500] for _ in range(11)]

field1 = [["." for _ in range(1000)] for _ in range(1000)]
field2 = [["." for _ in range(1000)] for _ in range(1000)]

for direction, steps in commands:
    for _ in range(steps):

        positions[0][0] += com_dic[direction][0]
        positions[0][1] += com_dic[direction][1]
        for x in range(1, 11):
            old_pos = positions[x]
            if abs(positions[x][0] - positions[x - 1][0]) > 1 or abs(positions[x][1] - positions[x - 1][1]) > 1:
                if abs(positions[x][0] - positions[x - 1][0]) > 1 and positions[x - 1][0] > positions[x][0]:
                    positions[x][0] = positions[x - 1][0] - 1

                    delta = positions[x - 1][1] - positions[x][1]
                    positions[x][1] = positions[x - 1][1] - int(delta / 2)

                if abs(positions[x][0] - positions[x - 1][0]) > 1 and positions[x - 1][0] < positions[x][0]:
                    positions[x][0] = positions[x - 1][0] + 1

                    delta = positions[x - 1][1] - positions[x][1]
                    positions[x][1] = positions[x - 1][1] - int(delta / 2)

                if abs(positions[x][1] - positions[x - 1][1]) > 1 and positions[x - 1][1] > positions[x][1]:
                    positions[x][1] = positions[x - 1][1] - 1

                    delta = positions[x - 1][0] - positions[x][0]
                    positions[x][0] = positions[x - 1][0] - int(delta / 2)

                if abs(positions[x][1] - positions[x - 1][1]) > 1 and positions[x - 1][1] < positions[x][1]:
                    positions[x][1] = positions[x - 1][1] + 1

                    delta = positions[x - 1][0] - positions[x][0]
                    positions[x][0] = positions[x - 1][0] - int(delta / 2)

            if x == 1:
                field1[positions[x][1]][positions[x][0]] = "#"
            if x == 9:
                field2[positions[x][1]][positions[x][0]] = "#"

cou1 = 0
cou2 = 0

for x in field1:
    for y in x:
        if y == "#":
            cou1 += 1

for x in field2:
    for y in x:
        if y == "#":
            cou2 += 1

print(f"Solution Part 1: {cou1}")
print(f"Solution Part 2: {cou2}")
