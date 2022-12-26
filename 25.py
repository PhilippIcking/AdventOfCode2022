with open("input25.txt") as f:
    inp = f.read().splitlines()

rules_dict = {
    "2": 2,
    "1": 1,
    "0": 0,
    "-": -1,
    "=": -2,
    }

inv_rules = {v: k for k, v in rules_dict.items()}

# get sum of input numbers
num_list = []
for x in inp:
    cou = 0
    for y in range(1, len(x) + 1):
        curr_char = x[-y]
        num_factor = rules_dict[curr_char]
        cou += (5 ** (y - 1)) * num_factor
    num_list.append(cou)

sol_num = sum(num_list)

# convert to base 5
result = []
while sol_num > 0:
    result.insert(0, sol_num % 5)
    sol_num = sol_num // 5

end_num = [0 for _ in range(len(result) + 1)]

# convert back to puzzle code
i = 1
for x in range(len(result)):
    if result[i-1] == 1:
        end_num[i] += 1
    elif result[i-1] == 2:
        end_num[i] += 2
    elif result[i-1] == 3:
        end_num[i] += -2
        end_num[i - 1] += 1
    elif result[i-1] == 4:
        end_num[i] += -1
        end_num[i - 1] += 1
    elif result[i-1] == 5:
        end_num[i - 1] += 1
    else:
        pass
    i += 1

if 3 in end_num:
    print(end_num)
    for x in range(1, len(end_num)):
        if end_num[x] == 3:
            end_num[x] = -2
            end_num[x - 1] += 1

sol_string = ""
for x in end_num:
    sol_string = sol_string.__add__(inv_rules[x])

print(f"The missing Code is: {sol_string}")