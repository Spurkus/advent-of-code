with open("day 2.txt", "r") as file:
    # Part 1
    data = [i.replace("\n", "") for i in file.readlines()]
    total = 0

    for mrID, game in enumerate(data):
        valid = True
        cubes = game.split(":")[1].split(";")

        for rounds in cubes:
            for colours in rounds.split(","):
                colour = colours.split()
                n = int(colour[0])
                if ("red" in colour and n > 12) or ("green" in colour and n > 13) or ("blue" in colour and n > 14):
                    valid = False

        if valid:
            total += mrID + 1
    print(total)


with open("input.txt", "r") as file:
    # Part 2
    data = [i.replace("\n", "") for i in file.readlines()]
    total = 0
    for game in data:
        highestRed = highestGreen = highestBlue = 1
        cubes = game.split(":")[1].split(";")

        for rounds in cubes:
            for colour in rounds.split(","):
                colour = colour.split()
                n = int(colour[0])
                if "red" in colour and n > highestRed:
                    highestRed = n
                if "green" in colour and n > highestGreen:
                    highestGreen = n
                if "blue" in colour and n > highestBlue:
                    highestBlue = n

        total += highestRed * highestGreen * highestBlue
    print(total)