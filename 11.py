with open("input11.txt") as f:
    inp = f.read().split("\n\n")

"""
monkey = [
    [],  # items
    "",  # operation
    int,  # divisor
    int,  # true_monkey
    int  # false_monkey
    ]
"""


def solve(rounds, a_rules):
    monkey_list = []
    for i in inp:
        a = i.split("\n")
        items = [int(x) for x in a[1].split(":")[1].split(",")]
        op = a[2].split(": new = old")[1]
        if op == " * old":
            op = " **2"
        div_num = int(a[3].split("by ")[1])
        true_monk = int(a[4].split("monkey ")[1])
        false_monk = int(a[5].split("monkey ")[1])
        monkey_list.append([items, op, div_num, true_monk, false_monk])

    faktor = 1
    for a in monkey_list:
        faktor = a[2] * faktor

    monkey_score = [0 for _ in range(len(monkey_list))]
    for k in range(rounds):
        for x in range(len(monkey_list)):
            items, op, div_num, true_monk, false_monk = monkey_list[x]
            for item in items:
                monkey_score[x] += 1
                worry_level = item
                if not a_rules:
                    worry_level = int(eval(str(worry_level) + op)) % faktor
                else:
                    worry_level = int(eval(str(worry_level) + op)/3) % faktor
                if worry_level % div_num == 0:
                    monkey_list[true_monk][0].append(worry_level)
                else:
                    monkey_list[false_monk][0].append(worry_level)
            monkey_list[x][0] = []

    monkey_score = sorted(monkey_score)
    print(f"Solution after {rounds} Rounds: {monkey_score[-1] * monkey_score[-2]}")


solve(20, True)
solve(10000, False)
