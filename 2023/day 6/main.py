with open("input.txt", "r") as file:
    data = [i.replace("\n", "") for i in file]
    time = [int(i) for i in data[0].split(": ")[1].split()]
    distance = [int(i) for i in data[1].split(": ")[1].split()]

def win(press, time, distance):
    amount = time - press
    yea = amount * press
    return yea > distance


def sol1():
    # yea part 1 i guess
    total = 1
    for i, n in enumerate(time):
        bruh = 0
        for m in range(n):
            if win(m, n, distance[i]):
                bruh += 1
        total *= bruh

    print(total)

def sol2():
    # part 2 perchance
    total = 0
    for i in range(55826490):
        if win(i, 55826490, 246144110121111):
            total += 1
    print(total)

if __name__ == "__main__":
    sol1()
    sol2()