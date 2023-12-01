def elf_calories(data):
    elves = []
    elf = 0
    for calorie in data:
        if calorie:
            elf += int(calorie)
        else:
            elves.append(elf)
            elf = 0

    return elves

with open("1.txt", "r") as file:
    data = file.readlines() + [""]
    bruh = elf_calories([i.replace("\n","") for i in data])
    one = max(bruh)
    bruh.remove(one)
    two = max(bruh)
    bruh.remove(two)
    three = max(bruh)
    print(one + two + three)
