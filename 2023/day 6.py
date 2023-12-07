with open("day 6.txt", "r") as file:
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
    newTime = int("".join([str(i) for i in time]))
    newDistance = int("".join([str(i) for i in distance]))
    total = 0
    for i in range(newTime):
        if win(i, newTime, newDistance):
            total += 1
    print(total)

if __name__ == "__main__":
    sol1()
    sol2()