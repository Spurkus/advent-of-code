with open("day 4.txt", "r") as file:
    data = [i.replace("\n", "") for i in file.readlines()]
    data = [i.split(": ")[1] for i in data]

def sol1():
    # part 1
    total = 0
    for card in data:
        cardTotal = 0
        winning, numbers = card.split("|")
        winning = [int(i) for i in winning.split()]
        numbers = [int(i) for i in numbers.split()]

        for i in numbers:
            if i in winning:
                if cardTotal == 0:
                    cardTotal += 1
                else:
                    cardTotal *= 2
        total += cardTotal
    print(total)

count = 0

def getCard(cards, cardNumber):
    global count
    count += 1

    cardTotal = 0

    winning, numbers = cards[cardNumber - 1].split("|")
    winning = [int(i) for i in winning.split()]
    numbers = [int(i) for i in numbers.split()]

    for i in numbers:
        if i in winning:
            cardTotal += 1

    for i in range(1, cardTotal + 1):
        if (cardNumber + i) < len(cards) + 1:
            getCard(cards, cardNumber + i)

def sol2():
    # part 2
    for i, _ in enumerate(data):
        getCard(data, i + 1)
    print(count)

if __name__ == "__main__":
    sol1()
    sol2()