with open("input06.txt") as f:
    inp_str = f.read()


def get_marker(y):
    for x in range(y-1, len(inp_str)):
        if len(set(inp_str[x - y:x])) == y:
            return x


print(get_marker(4))
print(get_marker(14))
