import re

with open("input05.txt") as f:
    rules, all_moves = f.read().split("\n\n")
moves = all_moves.splitlines()
pattern = "move ([0-9]+) from ([0-9]) to ([0-9])"
print(rules)


# Part 1
rows = ["BVSNTCHQ", "WDBG", "FWRTSQB", "LGWSZJDN", "MPDVF", "FWJ", "LNQBJV", "GTRCJQSN", "JSQCWDM"]

for move in moves:
    match = re.search(pattern, move)
    count = int(match.group(1))
    start = int(match.group(2))-1
    end = int(match.group(3))-1
    x = rows[start][-count:]
    rows[start] = rows[start].removesuffix(x)
    rows[end] = rows[end].__add__(x[::-1])

solution = ""
for r in rows:
    solution = solution.__add__(r[-1])
print(f"Part 1: {solution}")


# Part 2
rows = ["BVSNTCHQ", "WDBG", "FWRTSQB", "LGWSZJDN", "MPDVF", "FWJ", "LNQBJV", "GTRCJQSN", "JSQCWDM"]

for move in moves:
    match = re.search(pattern, move)
    count = int(match.group(1))
    start = int(match.group(2))-1
    end = int(match.group(3))-1
    x = rows[start][-count:]
    rows[start] = rows[start].removesuffix(x)
    rows[end] = rows[end].__add__(x)

solution = ""
for r in rows:
    solution = solution.__add__(r[-1])
print(f"Part 2: {solution}")
