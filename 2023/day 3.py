def is_symbol(char):
    return not (char in "123456789.")

def check_surround(row, col, data, yea, line, number):
    numbersLine = []
    reachedNumber = False
    for i in line:
        if i == number:
            reachedNumber = True
        if i.isdigit() and reachedNumber == False:
            numbersLine.append(len(i))

    oops = data[row].find(number, col + sum(numbersLine) - len(numbersLine))
    try:
        left = is_symbol(line[col - 1])
    except:
        left = False
    try:
        right = is_symbol(line[col + 1])
    except:
        right = False

    if (left or right):
        return True

    for i in range(len(number) + 2):
        try:
            if row != 0:
                above = is_symbol(data[row - 1][oops - 1 + i])
            else:
                above = False
        except:
            above = False
        try:
            below = is_symbol(data[row + 1][oops - 1 + i])
        except:
            below = False

        if (above or below):
            return True

    return False



def sol():
    with open("day 3.txt", "r") as file:
        total = 0
        data = [i.replace("\n", "") for i in file.readlines()]

        yea = []
        for line in data:
            formattedLine = []
            number = ""
            for c in line:
                if c.isdigit():
                    number += c
                else:
                    if number != "":
                        formattedLine.append(number)
                        number = ""
                    formattedLine.append(c)
        
            if number != "": # literally wrote this as bpaul was saying to make sure of number at the end
                formattedLine.append(number)
                number = ""

            yea.append(formattedLine)

        for row, line in enumerate(yea):
            for col, element in enumerate(line):
                if element.isdigit():
                    if check_surround(row, col, data, yea, line, element):
                        print(element)
                        total += int(element)
    print(total)



if __name__ == "__main__":
    sol()