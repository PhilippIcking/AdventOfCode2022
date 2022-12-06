import re
import numpy as np

with open("input04.txt") as f:
    all_pairs = f.read().splitlines()

pattern = "([0-9]+)-([0-9]+),([0-9]+)-([0-9]+)"
cou = 0
cou2 = 0

for pair in all_pairs:
    match = re.search(pattern, pair)
    range1 = set(np.arange(int(match.group(1)), int(match.group(2))+1))
    range2 = set(np.arange(int(match.group(3)), int(match.group(4))+1))
    if range1.issubset(range2) or range2.issubset(range1):
        cou += 1
    if not range1.isdisjoint(range2):
        cou2 += 1
print(f"Part 1: {cou}")
print(f"Part 2: {cou2}")
