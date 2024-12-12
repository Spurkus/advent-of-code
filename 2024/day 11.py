from collections import Counter
import json


def do_thing(i):
    if i == 0:
        return 1
    elif not (length := len(str(i))) % 2:
        return [int(str(i)[:length // 2]), int(str(i)[length // 2:])]
    else:
        return i * 2024


def sol1(data):
    for _ in range(25):
        yes = []
        for i in data:
            new = do_thing(i)
            if isinstance(new, list):
                yes.extend(new)
            else:
                yes.append(new)
            data = yes
    return len(data)


def sol2(data):
    for _ in range(40):
        yes = []
        for i in data:
            new = do_thing(i)
            if isinstance(new, list):
                yes.extend(new)
            else:
                yes.append(new)
            data = yes
    return data


def sol2part2(data):
    count = Counter(data)
    yea = []
    for i in count:
        yea.append(i)
    awesome = dict()
    for j, i in enumerate(count):
        print(j)
        ok = [i]
        for _ in range(35):
            yes = []
            for i in ok:
                new = do_thing(i)
                if isinstance(new, list):
                    yes.extend(new)
                else:
                    yes.append(new)
                ok = yes
        awesome[i] = len(ok)

    total = 0
    for i in awesome:
        total += awesome[i] * count[i]
    return total


if __name__ == "__main__":
    # with open("day 11.txt", "r") as file:
    # data = [int(n) for n in [i.replace("\n", "") for i in file.readlines()][0].split()]
    # print(sol1(data))
    # yay = sol2(data)
    # with open("day 11.txt", "w") as file:
    # file.write(str(yay))
    with open("day 11.txt", "r") as file:
        data = json.loads([i.replace("\n", "") for i in file.readlines()][0])
    print(sol2part2(data))
