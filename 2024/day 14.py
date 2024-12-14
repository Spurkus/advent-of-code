import time


def move_robot(p, v, t, wide, tall):
    x = (p[0] + v[0] * t) % wide
    y = (p[1] + v[1] * t) % tall
    return (x, y)


def sol1(robots):
    pos = []

    for p, v in robots:
        pos.append(move_robot(p, v, 100, 101, 103))

    quad_one = 0
    quad_two = 0
    quad_three = 0
    quad_four = 0

    for x, y in pos:
        if x == 50 or y == 51:
            continue
        if x < 50 and y < 51:
            quad_one += 1
        elif x > 50 and y < 51:
            quad_two += 1
        elif x < 50 and y > 51:
            quad_three += 1
        else:
            quad_four += 1

    return quad_one * quad_two * quad_three * quad_four


def sol2(robots):
    for i in range(10000):
        pos = set()
        for p, v in robots:
            pos.add(move_robot(p, v, i, 101, 103))

        ok = [[0 for _ in range(103)] for _ in range(101)]
        for x, y in pos:
            ok[x][y] = 1

        section = "#######"
        treeable = False
        for l in ok:
            l = ''.join([str(i) for i in l]).replace("1", "#").replace("0", " ")
            if section in l:
                treeable = True
                break

        if treeable:
            time.sleep(0.1)
            print(i)
            for l in ok:
                print(''.join([str(i) for i in l]).replace("1", "#").replace("0", " "))


if __name__ == "__main__":
    with open("day 14.txt", "r") as file:
        data = [i.replace("\n", "") for i in file.readlines()]

    robots = []

    for i in data:
        ok = i.split()
        p = ok[0].split(",")
        p = (int(p[0].split("=")[1]), int(p[1]))
        v = ok[1].split(",")
        v = (int(v[0].split("=")[1]), int(v[1]))
        robots.append((p, v))

    print(sol1(robots))
    sol2(robots)
