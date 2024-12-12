with open("day 10.txt", "r") as file:
    data = [i.replace("\n", "") for i in file.readlines()]
    zeros = []
    for i, j in enumerate(data):
        for k, l in enumerate(j):
            if l == "0":
                zeros.append((i, k))


def in_bounds(x, y):
    return 0 <= x < len(data) and 0 <= y < len(data[0])


def sol1():
    movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    nice = []

    def traverse(x, y, meow):
        if data[x][y] == "9":
            meow.add((x, y))
        for i, j in movements:
            if in_bounds(x + i, y + j) and data[x + i][y + j] == str(int(data[x][y]) + 1):
                traverse(x + i, y + j, meow)

    for i in zeros:
        meow = set()
        traverse(i[0], i[1], meow)
        nice.extend(meow)

    return len(nice)


def sol2():
    movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    meow = []

    def traverse(x, y):
        if data[x][y] == "9":
            meow.append((x, y))
        for i, j in movements:
            if in_bounds(x + i, y + j) and data[x + i][y + j] == str(int(data[x][y]) + 1):
                traverse(x + i, y + j)

    for i in zeros:
        traverse(i[0], i[1])

    return len(meow)


if __name__ == "__main__":
    print(sol1())
    print(sol2())
