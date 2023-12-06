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
    seeds = [int(i) for i in data[0][0].split(":")[1].split()]

    locations = []
    for i in range(0, len(seeds), 2):
        ranges = [[seeds[i], seeds[i] + seeds[i + 1]]]
        results = []
        for mappa in formattedData:
            while ranges:
                beginRange, endRange = ranges.pop()
                for destination, source, length in mappa:
                    bruh = source + length
                    yea = destination - beginRange
                    if bruh <= beginRange or endRange <= source:
                        continue
                    if beginRange < source:
                        ranges.append([beginRange, source])
                        beginRange = source
                    if bruh < endRange:
                        ranges.append([bruh, endRange])
                        endRange = bruh
                    results.append([beginRange + yea, endRange + yea])
                    break
                else:
                    results.append([beginRange, endRange])
            ranges = results
            results = []
        locations += ranges

    print(min(loc[0] for loc in locations))
    
if __name__ == "__main__":
    sol1()
    sol2()