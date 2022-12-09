with open("input08.txt") as f:
    trees = f.read().splitlines()


def treevisible(x, y):
    currtree = treemap[y][x]

    # Down
    for b in range(len(treemap[y]) - y):
        if treemap[-b][x] >= currtree:
            break
    else:
        return True
    # Up
    for b in range(y):
        if treemap[b][x] >= currtree:
            break
    else:
        return True
    # Right
    for b in range(len(treemap[x]) - x):
        if treemap[y][-b] >= currtree:
            break
    else:
        return True
    # Left
    for b in range(x):
        if treemap[y][b] >= currtree:
            break
    else:
        return True
    return False


cou = 0
treemap = []
for counter, x in enumerate(trees):
    treemap.append([])
    for y in x:
        treemap[counter].append(int(y))

for y in range(1, len(treemap) - 1):
    for x in range(1, len(treemap[0]) - 1):
        if treevisible(x, y):
            cou += 1
            print(cou)
            print(y ,x)
