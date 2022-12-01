with open("input01.txt") as f:
    elf_list = f.read().split("\n\n")

# Part 1
max_cou = 0
for count, elf in enumerate(elf_list):
    y = elf.split("\n")
    cou = 0
    for z in y:
        cou += int(z)
    if cou > max_cou:
        max_cou = cou
        elf_number = count
print(f"The Elf with most Calories ist Elf {count} with a total of {max_cou} Calories.")

# Part 2
calorie_list = []
for elf in elf_list:
    y = elf.split("\n")
    cou = 0
    for z in y:
        cou += int(z)
    calorie_list.append(cou)
calorie_list = sorted(calorie_list)
print(f"The Sum of the top three Elves carry a total of {sum(calorie_list[-3:])} Calories.")
