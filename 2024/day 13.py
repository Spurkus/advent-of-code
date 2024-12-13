def find_fewest_tokens(a, b, prize):
    lowest = 10000000000
    for i in range(100):
        for j in range(100):
            x = i * a[0] + j * b[0]
            y = i * a[1] + j * b[1]
            if x == prize[0] and y == prize[1]:
                lowest = min(lowest, i * 3 + j)

    if lowest == 10000000000:
        return 0

    return lowest


def find_fewest_tokens_more(a, b, prize):
    detetermining = a[0] * b[1] - a[1] * b[0]

    if detetermining == 0:
        return 0

    x = (b[1] * prize[0] - b[0] * prize[1]) / detetermining
    y = (-a[1] * prize[0] + a[0] * prize[1]) / detetermining

    if x.is_integer() and y.is_integer() and x >= 0 and y >= 0:
        return int(3 * x + y)

    return 0


def sol1(data):
    total = 0
    for a, b, prize in data:
        total += find_fewest_tokens(a, b, prize)

    return total


def sol2(data):
    total = 0
    for a, b, prize in data:
        x, y = prize
        token = find_fewest_tokens_more(a, b, (x + 10000000000000, y + 10000000000000))
        total += token

    return total


if __name__ == "__main__":
    with open("day 13.txt", "r") as file:
        data = [i.replace("\n", "") for i in file.readlines()]

    ok = [i.split('meow') for i in 'meow'.join(data).split("meowmeow")]
    formatted = []

    for i in ok:
        first = [n.replace("+", "+           ") for n in i[0].split(",")]
        a = (int(first[0][-4:]), int(first[1][-4:]))
        second = [n.replace("+", "+           ") for n in i[1].split(",")]
        b = (int(second[0][-4:]), int(second[1][-4:]))
        third = [n.replace("=", "=            ") for n in i[2].split(",")]
        prize = (int(third[0][-8:]), int(third[1][-8:]))
        formatted.append((a, b, prize))

    print(sol1(formatted))
    print(sol2(formatted))
