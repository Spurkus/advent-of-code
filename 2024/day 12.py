RIGHT = 1
LEFT = 2
TOP = 3
BOTTOM = 4


def in_grid(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def find_surrounding(grid, x, y, n):
    surrounding = set()
    surrounding.add((x, y))

    around = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def check(x, y):
        for a, b in around:
            if in_grid(grid, x + a, y + b):
                if grid[x + a][y + b] == n and (x + a, y + b) not in surrounding:
                    surrounding.add((x + a, y + b))
                    check(x + a, y + b)

    check(x, y)
    return surrounding


def calculate_perimeter(coords):
    surround = set()
    around = [(0, 1, RIGHT), (1, 0, BOTTOM), (0, -1, LEFT), (-1, 0, TOP)]

    for x, y in coords:
        for a, b, o in around:
            if (x + a, y + b) not in coords:
                surround.add((x, y, o))

    return surround


def sol1(data):
    all = []
    for i, j in enumerate(data):
        for n, m in enumerate(j):
            area = find_surrounding(data, i, n, m)
            if len(area) > 0 and area not in all:
                all.append(area)

    total = 0
    for i in all:
        p = len(calculate_perimeter(i))
        total += p * len(i)

    return total


def calculate_sides(perimeter):
    rights = sorted([i for i in perimeter if i[2] == RIGHT], key=lambda x: (x[1], x[0]))
    lefts = sorted([i for i in perimeter if i[2] == LEFT], key=lambda x: (x[1], x[0]))
    tops = sorted([i for i in perimeter if i[2] == TOP])
    bottoms = sorted([i for i in perimeter if i[2] == BOTTOM])

    right_side = 0
    if len(rights) == 1:
        right_side += 1
    else:
        right_side += 1
        prev = rights[0]
        for i in rights[1:]:
            if i[1] != prev[1]:
                right_side += 1
                prev = i
                continue

            if i[0] - 1 != prev[0]:
                right_side += 1
            prev = i

    left_side = 0
    if len(lefts) == 1:
        left_side += 1
    else:
        left_side += 1
        prev = lefts[0]
        for i in lefts[1:]:
            if i[1] != prev[1]:
                left_side += 1
                prev = i
                continue

            if i[0] - 1 != prev[0]:
                left_side += 1
            prev = i

    top_side = 0
    if len(tops) == 1:
        top_side += 1
    else:
        top_side += 1
        prev = tops[0]
        for i in tops[1:]:
            if i[0] != prev[0]:
                top_side += 1
                prev = i
                continue

            if i[1] - 1 != prev[1]:
                top_side += 1
            prev = i

    bottom_side = 0
    if len(bottoms) == 1:
        bottom_side += 1
    else:
        bottom_side += 1
        prev = bottoms[0]
        for i in bottoms[1:]:
            if i[0] != prev[0]:
                bottom_side += 1
                prev = i
                continue

            if i[1] - 1 != prev[1]:
                bottom_side += 1
            prev = i

    return right_side + left_side + top_side + bottom_side


def sol2(data):
    all = []
    for i, j in enumerate(data):
        for n, m in enumerate(j):
            area = find_surrounding(data, i, n, m)
            if len(area) > 0 and area not in all:
                all.append(area)

    total = 0
    for i in all:
        p = calculate_perimeter(i)
        s = calculate_sides(p)
        total += s * len(i)

    return total


if __name__ == "__main__":
    with open("day 12.txt", "r") as file:
        data = [i.replace("\n", "") for i in file.readlines()]
    print(sol1(data))
    print(sol2(data))
