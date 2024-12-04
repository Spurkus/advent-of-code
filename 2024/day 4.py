with open("day 4.txt", "r") as file:
    data = [i.replace("\n", "") for i in file.readlines()]


def sol1():
    bruh = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    ]
    row_num = len(data)
    col_num = len(data[0])
    count = 0

    for row in range(row_num):
        for col in range(col_num):
            for x, y in bruh:
                match = True
                for i in range(4):
                    ok = row + (x * i)
                    boomer = col + (y * i)
                    if not (0 <= ok < row_num and
                            0 <= boomer < col_num) or data[ok][boomer] != "XMAS"[i]:
                        match = False
                        break
                if match:
                    count += 1

    print(count)


def sol2():
    big_back_one = [
        (-1, -1, "M"),
        (-1, 1, "M"),
        (1, -1, "S"),
        (1, 1, "S"),
    ]

    big_back_two = [
        (-1, -1, "S"),
        (-1, 1, "S"),
        (1, -1, "M"),
        (1, 1, "M"),
    ]

    big_back_three = [
        (-1, -1, "M"),
        (-1, 1, "S"),
        (1, -1, "M"),
        (1, 1, "S"),
    ]

    big_back_four = [
        (-1, -1, "S"),
        (-1, 1, "M"),
        (1, -1, "S"),
        (1, 1, "M"),
    ]

    row_num = len(data)
    col_num = len(data[0])
    count = 0

    for row in range(row_num):
        for col in range(col_num):
            if 1 <= row < row_num - 1 and 1 <= col < col_num - 1 and data[row][col] == "A":
                match = False
                for herm in [big_back_one, big_back_two, big_back_three, big_back_four]:
                    interesting = True
                    for x, y, a in herm:
                        if data[row + x][col + y] != a:
                            interesting = False
                            break
                    if interesting:
                        match = True
                        break
                if match:
                    count += 1
    print(count)


if __name__ == "__main__":
    # sol1()
    sol2()
