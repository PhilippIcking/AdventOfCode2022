with open("input07.txt") as f:
    inp = f.read().splitlines()

size_dic = {"/": 0}
file_name = []

for x in inp:
    if x[0:4] == "$ ls":
        continue
    elif x[0:4] == "$ cd":
        if x[5:7] != "..":
            curr_dir = x.split(" ")[2]
            file_name.append(curr_dir)
            file_name_string = ""
            for a in file_name:
                file_name_string = file_name_string.__add__(a)
            size_dic[file_name_string] = 0
        else:
            file_name.pop()
    else:
        if x.split(" ")[0].isdigit():
            file_name_string = ""
            for a in file_name:
                file_name_string = file_name_string.__add__(a)
                size_dic[file_name_string] += int(x.split(" ")[0])

total = 0
for a in size_dic:
    if size_dic[a] <= 100000:
        total += size_dic[a]
print(f"Solution Part 1: {total}")

poss_del = []
for a in size_dic:
    if (70000000 - size_dic["/"] + size_dic[a]) >= 30000000:
        poss_del.append(size_dic[a])
print(f"Solution Part 2: {sorted(poss_del)[0]}")
