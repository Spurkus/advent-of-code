with open("day 9.txt", "r") as file:
    data = [i.replace("\n", "") for i in file.readlines()][0]
    blocks = []
    file_lengths = []
    id = 0
    i = 0

    while i < len(data):
        length = int(data[i])
        i += 1
        if length > 0:
            blocks.extend([str(id)] * length)
            id += 1

        if i < len(data):
            space = int(data[i])
            i += 1
            blocks.extend(['.'] * space)


def sol1():
    blocks1 = blocks.copy()
    left, right = 0, len(blocks) - 1
    while left < right:
        if blocks1[left] == '.' and blocks1[right] != '.':
            blocks1[left], blocks1[right] = blocks1[right], blocks1[left]
        elif blocks1[right] == '.':
            right -= 1
        elif blocks1[left] != '.':
            left += 1

    total = 0
    for i, j in enumerate(blocks1):
        if j == ".":
            break
        total += i * int(j)
    return total


def sol2():
    count = dict()
    for i in blocks:
        if i == ".":
            continue
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    ids = sorted(count.keys(), reverse=True)

    for id in ids:
        spaces = 0
        i = 0
        start = False

        bruhs = []

        while i < len(blocks):
            if not start and blocks[i] == ".":
                spaces += 1
                start = True
            elif start and blocks[i] == ".":
                spaces += 1
            elif start and blocks[i] != ".":
                bruhs.append((i, spaces))
                spaces = 0
            i += 1

        for j, k in bruhs:
            if count[id] <= k and blocks.index(str(id)) > j:
                hm = 0

                yay = 0
                while yay < len(blocks):
                    if blocks[yay] == id:
                        blocks[yay] = "."
                    yay += 1

                while hm < count[id]:
                    blocks[j - k + hm] = id
                    hm += 1
                break

    total = 0
    for i, j in enumerate(blocks):
        if j == ".":
            continue
        total += i * int(j)
    return total


if __name__ == "__main__":
    print(sol1())
    print(sol2())
