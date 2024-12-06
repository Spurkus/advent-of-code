with open("day 6.txt", "r") as file:
    data = [i.replace("\n", "") for i in file.readlines()]
    hashtages = set()
    little_guy = (0, 0, "")
    for i, j in enumerate(data):
        for n, m in enumerate(j):
            if m == "#":
                hashtages.add((i, n))
            if m == "^":
                little_guy = (i, n, m)


def move(meow, extra=(-1, -1)):
    if meow[2] == "^":
        if meow[0] == 0:
            return None
        if (meow[0] - 1, meow[1]) in hashtages or (meow[0] - 1, meow[1]) == extra:
            return (meow[0], meow[1], ">")
        return (meow[0] - 1, meow[1], "^")
    if meow[2] == "v":
        if meow[0] == len(data) - 1:
            return None
        if (meow[0] + 1, meow[1]) in hashtages or (meow[0] + 1, meow[1]) == extra:
            return (meow[0], meow[1], "<")
        return (meow[0] + 1, meow[1], "v")
    if meow[2] == "<":
        if meow[1] == 0:
            return None
        if (meow[0], meow[1] - 1) in hashtages or (meow[0], meow[1] - 1) == extra:
            return (meow[0], meow[1], "^")
        return (meow[0], meow[1] - 1, "<")
    if meow[2] == ">":
        if meow[1] == len(data[0]) - 1:
            return None
        if (meow[0], meow[1] + 1) in hashtages or (meow[0], meow[1] + 1) == extra:
            return (meow[0], meow[1], "v")
        return (meow[0], meow[1] + 1, ">")


def sol1():
    pos = set()
    ok = little_guy
    while True:
        ok = move(ok)
        if ok == None:
            break
        pos.add((ok[0], ok[1]))
    print(len(pos))
    return pos


def sol2(path):
    loops = 0

    for i, j in path:
        pos = set()
        ok = little_guy
        while True:
            ok = move(ok, (i, j))
            if ok == None:
                break
            if ok not in pos:
                pos.add(ok)
            else:
                loops += 1
                break
    print(loops)


if __name__ == "__main__":
    path = sol1()
    sol2(path)
