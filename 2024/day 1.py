with open("day 1.txt", "r") as file:
    data = [i.replace("\n", "").split("   ") for i in file.readlines()]
    listone = [int(i[0]) for i in data]
    listone.sort()
    listtwo = [int(i[1]) for i in data]
    dicttwo = dict()
    for i in listtwo:
        dicttwo[i] = dicttwo.get(i, 0) + 1


def sol1():
    # part 1
    total = 0
    for i in range(len(listone)):
        total += abs(listone[i] - listtwo[i])
    print(total)


def sol2():
    total = 0
    for i in listone:
        total += i * dicttwo.get(i, 0)
    print(total)


if __name__ == "__main__":
    sol1()
    sol2()
