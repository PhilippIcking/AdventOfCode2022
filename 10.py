with open("input10.txt") as f:
    inp = f.read().splitlines()

cou = [1]

for x in inp:
    if x[:4] == "noop":
        cou.append(0)
    else:
        cou.append(0)
        cou.append(int(x[5:]))

# Part 1
print("Part 1: " + str(sum(cou[:20])*20 + sum(cou[:60])*60 + sum(cou[:100])*100 +
      sum(cou[:140])*140 + sum(cou[:180])*180 + sum(cou[:220])*220))

crt = ""
for counter, _ in enumerate(cou):
    if [sum(cou[:counter]), sum(cou[:counter])+1, sum(cou[:counter])+2].__contains__(counter%40):
        crt = crt.__add__("#")
    else:
        crt = crt.__add__(".")

crt = crt[1:]
print("Part 2:")
for x in range(6):
    print(crt[x*40:(x+1)*40])
