def sol1(boxes, nonono, robot, movements):
    correspond = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}

    for i in movements:
        dx, dy = correspond[i]
        temp_robot = (robot[0] + dx, robot[1] + dy)
        if temp_robot not in nonono and temp_robot not in boxes:
            robot = temp_robot
            continue

        if temp_robot in nonono:
            continue

        if temp_robot in boxes:
            n = 0
            can_move = True
            while True:
                if (temp_robot[0] + dx * n, temp_robot[1] + dy * n) in boxes:
                    n += 1
                    continue
                if (temp_robot[0] + dx * n, temp_robot[1] + dy * n) in nonono:
                    can_move = False
                    break
                break
            if can_move:
                for j in range(n):
                    boxes.remove((temp_robot[0] + dx * j, temp_robot[1] + dy * j))
                for j in range(n):
                    boxes.append((temp_robot[0] + dx * (j + 1), temp_robot[1] + dy * (j + 1)))
                robot = temp_robot

    total = 0
    for x, y in boxes:
        total += 100 * x + y
    return total


def can_move(boxes, nonono, box, dx, dy):
    all_boxes = set()
    all_boxes.add(box)
    moveable = True

    def meow(x, y, dx, dy):
        nonlocal moveable
        if (x + dx, y + dy) in boxes and (x + dx, y + dy) not in all_boxes:
            all_boxes.add((x + dx, y + dy))
            meow(x + dx, y + dy, dx, dy)
        if (x + dx, y + dy - 1) in boxes and (x + dx, y + dy - 1) not in all_boxes:
            all_boxes.add((x + dx, y + dy - 1))
            meow(x + dx, y + dy - 1, dx, dy)
        if (x + dx, y + dy + 1) in boxes and (x + dx, y + dy + 1) not in all_boxes:
            all_boxes.add((x + dx, y + dy + 1))
            meow(x + dx, y + dy + 1, dx, dy)

        if (x + dx, y + dy) in nonono or (x + dx, y + dy + 1) in nonono:
            moveable = False
            return

    meow(box[0], box[1], dx, dy)
    if moveable:
        return True, all_boxes
    return False


def sol2(boxes, nonono, robot, movements):
    correspond = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}

    for i in movements:
        other_boxes = [(x, y + 1) for x, y in boxes]

        dx, dy = correspond[i]
        temp_robot = (robot[0] + dx, robot[1] + dy)
        if temp_robot not in nonono and temp_robot not in boxes and temp_robot not in other_boxes:
            robot = temp_robot
            continue

        if temp_robot in nonono:
            continue

        if temp_robot in boxes or temp_robot in other_boxes:
            if temp_robot in boxes:
                ok = can_move(boxes, nonono, temp_robot, dx, dy)
            else:
                ok = can_move(boxes, nonono, (temp_robot[0], temp_robot[1] - 1), dx, dy)
            if ok:
                for x, y in ok[1]:
                    boxes.remove((x, y))
                for x, y in ok[1]:
                    boxes.append((x + dx, y + dy))
                robot = temp_robot

    total = 0
    for x, y in boxes:
        total += 100 * x + y
    return total


if __name__ == "__main__":
    with open("day 15.txt", "r") as file:
        data = [i.replace("\n", "") for i in file.readlines()]

    movement_yet = False

    boxes = []
    nonono = set()
    robot = (0, 0)
    movements = ""

    big_boxes = []
    big_nonono = set()
    big_robot = (0, 0)

    for i, j in enumerate(data):
        if j == "":
            movement_yet = True
        if movement_yet:
            movements += j
        else:
            for n, m in enumerate(j):
                if m == "O":
                    boxes.append((i, n))
                    big_boxes.append((i, n * 2))
                if m == "@":
                    robot = (i, n)
                    big_robot = (i, n * 2)
                if m == "#":
                    nonono.add((i, n))
                    big_nonono.add((i, n * 2))
                    big_nonono.add((i, n * 2 + 1))

    # print(sol1(boxes, nonono, robot, movements))
    print(sol2(big_boxes, big_nonono, big_robot, movements))
