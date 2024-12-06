with open("day 5.txt", "r") as file:
    data = []
    meow = []
    bruh = True
    for i in file.readlines():
        if i == "\n":
            bruh = False
        if bruh:
            data.append(i.replace("\n", "").split("|"))
        else:
            meow.append(i.replace("\n", ""))
    data = [(int(x), int(y)) for x, y in data]
    meow = [[int(x) for x in i.split(",")] for i in meow[1:]]


def valid_line(line):
    pages = []
    for x, y in data:
        if x in line and y in line:
            pages.append((x, y))

    for left, right in pages:
        if line.index(left) > line.index(right):
            return False
    return True


def fix_line(line):
    pages = []
    for x, y in data:
        if x in line and y in line:
            pages.append((x, y))
    for left, right in pages:
        if line.index(left) > line.index(right):
            line[line.index(left)], line[line.index(right)] = line[line.index(right)], line[
                line.index(left)]
    for left, right in pages:
        if line.index(left) > line.index(right):
            line[line.index(left)], line[line.index(right)] = line[line.index(right)], line[
                line.index(left)]
    for left, right in pages:
        if line.index(left) > line.index(right):
            line[line.index(left)], line[line.index(right)] = line[line.index(right)], line[
                line.index(left)]
    for left, right in pages:
        if line.index(left) > line.index(right):
            line[line.index(left)], line[line.index(right)] = line[line.index(right)], line[
                line.index(left)]
    return line


def sol1():
    total = 0
    for i in meow:
        if valid_line(i):
            total += i[len(i) // 2]
    print(total)


def sol2():
    total = 0
    for i in meow:
        if not valid_line(i):
            i = fix_line(i)
            total += i[len(i) // 2]
    print(total)


if __name__ == "__main__":
    sol2()
