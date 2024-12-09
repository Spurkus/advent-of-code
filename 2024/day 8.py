with open("day 8.txt", "r") as file:
    data = [i.replace("\n", "") for i in file.readlines()]
    meow = dict()
    rows, cols = len(data), len(data[0])
    for row, i in enumerate(data):
        for col, j in enumerate(i):
            if j != '.':
                if j in meow:
                    meow[j].append((row, col))
                else:
                    meow[j] = [(row, col)]


def within_bounds(x, y):
    return 0 <= x < cols and 0 <= y < rows


def sol1():
    ok = set()
    for _, ants in meow.items():
        for y1, x1 in ants:
            for y2, x2 in ants:
                if x1 == x2 and y1 == y2:
                    continue
                dx, dy = x2 - x1, y2 - y1
                x, y = x1 - dx, y1 - dy
                if within_bounds(x, y):
                    ok.add((x, y))

    return len(ok)


def sol2():
    ok = set()
    for _, ants in meow.items():
        for y1, x1 in ants:
            for y2, x2 in ants:
                if x1 == x2 and y1 == y2:
                    continue
                dx, dy = x2 - x1, y2 - y1
                x, y = x1, y1
                while within_bounds(x, y):
                    ok.add((x, y))
                    x += dx
                    y += dy

    return len(ok)


if __name__ == "__main__":
    print(sol1())
    print(sol2())
