import string
with open("input03.txt") as f:
    items = f.read().splitlines()

alphabet = list(string.ascii_letters)
values_alpha = []
for counter, x in enumerate(alphabet):
    values_alpha.append((x,counter+1))

# Part 1

splited_items = []

for counter, item in enumerate(items):
    a = item[:int(len(item) / 2)]
    b = item[int(len(item) / 2):]
    splited_items.append((a, b))

cou = 0
for x, y in splited_items:
    for z in x:
        if y.__contains__(z):
            for i, j in values_alpha:
                if i == z:
                    cou += j
                    break
            break
print(cou)

# Part 2
cou = 0
groups = []
for x in range(0, len(items), 3):
    groups.append(items[x:x+3])

for x in groups:
    for y in x[0]:
        if x[1].__contains__(y) and x[2].__contains__(y):
            for i, j in values_alpha:
                if i == y:
                    cou += j
                    break
            break
print(cou)
