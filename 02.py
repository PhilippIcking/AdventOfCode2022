with open("input02.txt") as f:
    match_list = f.read().splitlines()


a = [("X", 1), ("Y", 2), ("Z", 3)]
wins = ["A Y", "B Z", "C X"]
draws = ["A X", "B Y", "C Z"]
loses = ["A Z", "B X", "C Y"]

# Part 1

score = 0

for game in match_list:
    for state, points in a:
        if game[2] == state:
            score += points
    if wins.__contains__(game):
        score += 6
    elif draws.__contains__(game):
        score += 3
    else:
        continue

print(f"Solution to Part 1 is {score}")

# Part 2

b = [("X", 0), ("Y", 3), ("Z", 6)]

score = 0

for game in match_list:
    for outcome, points in b:
        if game[2] == outcome:
            score += points
    if game[2] == "X":
        for j in loses:
            if game[0] == j[0]:
                for state, value in a:
                    if j[2] == state:
                        score += value
    elif game[2] == "Y":
        for j in draws:
            if game[0] == j[0]:
                for state, value in a:
                    if j[2] == state:
                        score += value
    elif game[2] == "Z":
        for j in wins:
            if game[0] == j[0]:
                for state, value in a:
                    if j[2] == state:
                        score += value
    else:
        continue

print(f"Solution to Part 2 is {score}")
