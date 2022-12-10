with open("input08.txt") as f:
    raw_trees = f.read().splitlines()

trees = []
for counter, x in enumerate(raw_trees):
    trees.append([])
    for y in x:
        trees[counter].append(int(y))


def is_visible(y_koor, x_koor):
    val_tree = trees[y_koor][x_koor]

    right_dir = 0
    tree_count_final = 1
    tree_count_curr = 0
    # down
    for a in range(1, len(trees) - y_koor):
        tree_count_curr += 1
        if trees[y_koor + a][x_koor] >= val_tree:
            break
    else:
        right_dir += 1

    tree_count_final = tree_count_final * tree_count_curr
    tree_count_curr = 0

    # right
    for a in range(1, len(trees[y_koor]) - x_koor):
        tree_count_curr += 1
        if trees[y_koor][x_koor + a] >= val_tree:
            break

    else:
        right_dir += 1

    tree_count_final = tree_count_final * tree_count_curr
    tree_count_curr = 0

    # up
    for a in range(1, y_koor + 1):
        tree_count_curr += 1
        if trees[y_koor - a][x_koor] >= val_tree:
            break
    else:
        right_dir += 1

    tree_count_final = tree_count_final * tree_count_curr
    tree_count_curr = 0

    # left
    for a in range(1, x_koor + 1):
        tree_count_curr += 1
        if trees[y_koor][x_koor - a] >= val_tree:
            break
    else:
        right_dir += 1

    tree_count_final = tree_count_final * tree_count_curr
    tree_count_curr = 0
    tree_count_list.append(tree_count_final)
    if right_dir >= 1:
        return True
    else:
        return False


tree_count_list = []
cou = 2 * len(trees) + 2 * len(trees[0]) - 4
for y in range(1, len(trees) - 1):
    for x in range(1, len(trees[y]) - 1):
        if is_visible(y, x):
            cou += 1

print(f"Part 1: {cou}")
print(f"Part 2: {max(tree_count_list)}")
