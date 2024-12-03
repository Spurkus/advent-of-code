with open("day 3.txt", "r") as file:
    data = [i.replace("\n", "") for i in file.readlines()]


def sol1():
    total = 0
    for bruh in data:
        i = 0
        while i < len(bruh):
            if i + 3 < len(bruh) and bruh[i] == "m" and bruh[i + 1] == "u" and bruh[
                    i + 2] == "l" and bruh[i + 3] == "(":
                i += 4
                num1_valid = True
                num1 = ""

                while i < len(bruh) and bruh[i] != ",":
                    if not bruh[i].isnumeric():
                        num1_valid = False
                        break
                    num1 += bruh[i]
                    i += 1

                if not num1_valid:
                    continue

                i += 1
                num2_valid = True
                num2 = ""

                while i < len(bruh) and bruh[i] != ")":
                    if not bruh[i].isnumeric():
                        num2_valid = False
                        break
                    num2 += bruh[i]
                    i += 1

                if not num2_valid:
                    continue

                total += int(num1) * int(num2)

            i += 1
    print(total)


def sol2():
    total = 0
    enabled = True
    for bruh in data:
        i = 0
        while i < len(bruh):
            if enabled:
                if i + 6 < len(bruh) and bruh[i] == "d" and bruh[i + 1] == "o" and bruh[
                        i + 2] == "n" and bruh[i + 3] == "'" and bruh[i + 4] == "t" and bruh[
                            i + 5] == "(" and bruh[i + 6] == ")":
                    enabled = False
                    i += 5
                else:
                    if i + 3 < len(bruh) and bruh[i] == "m" and bruh[i + 1] == "u" and bruh[
                            i + 2] == "l" and bruh[i + 3] == "(":
                        i += 4
                        num1_valid = True
                        num1 = ""

                        while i < len(bruh) and bruh[i] != ",":
                            if not bruh[i].isnumeric():
                                num1_valid = False
                                break
                            num1 += bruh[i]
                            i += 1

                        if not num1_valid:
                            continue

                        i += 1
                        num2_valid = True
                        num2 = ""

                        while i < len(bruh) and bruh[i] != ")":
                            if not bruh[i].isnumeric():
                                num2_valid = False
                                break
                            num2 += bruh[i]
                            i += 1

                        if not num2_valid:
                            continue

                        # Valid mul instruction; add to total
                        total += int(num1) * int(num2)
            else:
                if i + 4 < len(bruh) and bruh[i] == "d" and bruh[i + 1] == "o" and bruh[
                        i + 2] == "(" and bruh[i + 3] == ")":
                    enabled = True
                    i += 3
            i += 1
    print(total)


if __name__ == "__main__":
    # sol1()
    sol2()
