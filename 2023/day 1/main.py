with open("input.txt", "r") as file:
    data = [i.replace("\n", "") for i in file.readlines()]
    numbers = []
    for line in data:
        line = line.replace("one", "one1one").replace("two", "two2two").replace("three", "three3three",).replace("four", "four4four").replace("five", "five5five").replace("six", "six6six").replace("seven", "seven7seven").replace("eight", "eight8eight").replace("nine", "nine9nine")
        first = ""
        last = ""
        for character in line:
            if character.isnumeric():
                if first == "":
                    first = character
                    last = character
                else:
                    last = character
        numbers.append(int(first + last))
    print(sum(numbers))