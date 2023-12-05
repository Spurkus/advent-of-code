with open("input.txt", "r") as file:
    data = [i.split("\n") for i in "".join(file).split("\n\n")]
    formattedData = [[[int(v) for v in n.split()] for n in i[1:]] for i in data[1:]]

def sol1():
    seedsP1 = [int(i) for i in data[0][0].split(":")[1].split()]
    for mappa in formattedData:
        mappedSeeds = []
        for seed in seedsP1:
            mapped = False
            for destination, source, length in mappa:
                if seed in range(source, source + length):
                    mappedSeeds.append(seed + destination - source)
                    mapped = True
            if mapped == False:
                mappedSeeds.append(seed)

        seedsP1 = mappedSeeds
    print(min(seedsP1))

def sol2():
    seedsP2 = [int(i) for i in data[0][0].split(":")[1].split()]
    seedsP2 = [(i, i + seedsP2[n + 1]) for n, i in enumerate(seedsP2) if n % 2 == 0]

    for i, step in enumerate(formattedData):
        newseeds = []
        smol = float("inf")
        for seed1, seed2 in seedsP2:
            mapped = False
            for dest1, source1, sourcel in step:
                if i != len(formattedData):
                    int1, int2 = (max(source1, seed1), min(source1 + sourcel, seed2))
                else:
                    int1, int2 = (min(source1, seed1), min(source1 + sourcel, seed2))

                if int1 < int2 and mapped == False and i + 1 != len(formattedData):
                    newseeds.append((int1 + dest1 - source1, int2 + dest1 - source1))
                    mapped = True

                if seed1 < smol:
                    smol = seed1
            if i == len(formattedData):
                newseeds.append((smol, seed2))
            elif mapped == False:
                newseeds.append((seed1, seed2))

        print(newseeds)
        seedsP2 = newseeds
    
    print(min(k[0] for k in seedsP2))




if __name__ == "__main__":
    sol2()