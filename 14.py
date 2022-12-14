with open("input14.txt") as f:
    inp = f.read().splitlines()

cave = [["." for _ in range(1000)] for _ in range(1000)]
y_moves_list = []

for a in inp:
    locs = a.split(" -> ")
    moves = []
    for loc in locs:
        moves.append(loc.split(","))
    for x in range(len(moves) - 1):
        y_moves = [int(moves[x][0]), int(moves[x + 1][0])]
        y_moves_list.append(int(moves[x][1]))
        x_moves = [int(moves[x][1]), int(moves[x + 1][1])]
        for x2 in range(max(x_moves) - min(x_moves) + 1):
            for y2 in range(max(y_moves) - min(y_moves) + 1):
                cave[min(x_moves) + x2][min(y_moves) + y2] = "#"

# Part 1
# Start of Sand Simulation

overflow = False

y_koor = 0
x_koor = 500
while not overflow:
    try:
        if cave[y_koor + 1][x_koor] != ".":
            if cave[y_koor + 1][x_koor - 1] == ".":
                y_koor = y_koor + 1
                x_koor = x_koor - 1
            else:
                if cave[y_koor + 1][x_koor + 1] == ".":
                    y_koor = y_koor + 1
                    x_koor = x_koor + 1
                else:
                    cave[y_koor][x_koor] = "o"
                    y_koor = 0
                    x_koor = 500
        else:
            y_koor = y_koor + 1
    except:
        overflow = True

cou = 0
for x in cave:
    for y in x:
        if y == "o":
            cou += 1
print("Part 1: " + str(cou))


# Part 2
for x in range(len(cave[max(y_moves_list)+2])):
    cave[max(y_moves_list) + 2] = ["#" for _ in range(1000)]
# Start of Sand Simulation

full = False

y_koor = 0
x_koor = 500

while not full:
    if cave[y_koor + 1][x_koor] != ".":
        if cave[y_koor + 1][x_koor - 1] == ".":
            y_koor = y_koor + 1
            x_koor = x_koor - 1
        else:
            if cave[y_koor + 1][x_koor + 1] == ".":
                y_koor = y_koor + 1
                x_koor = x_koor + 1
            else:
                cave[y_koor][x_koor] = "o"
                y_koor = 0
                x_koor = 500
    else:
        y_koor = y_koor + 1

    if cave[0][500] == "o":
        full = True


cou = 0
for x in cave:
    for y in x:
        if y == "o":
            cou += 1

print("Part 2: " + str(cou))
