with open("day 2.txt", "r") as file:
    data = [i.replace("\n", "").split() for i in file.readlines()]


def sol1():
    safe = 0
    for report in data:
        bruh = [int(i) for i in report]
        increasing = bruh[0] < bruh[1]
        ok_boomer = True

        for i, ok in enumerate(bruh):
            if i == len(bruh) - 1:
                break

            if increasing:
                if ok >= bruh[i + 1]:
                    ok_boomer = False
                    break
            else:
                if ok <= bruh[i + 1]:
                    ok_boomer = False
                    break

            if abs(ok - bruh[i + 1]) == 0 or abs(ok - bruh[i + 1]) > 3:
                ok_boomer = False
                break
        if ok_boomer:
            safe += 1

    print(safe)


def sol2():
    safe = 0
    for report in data:
        bruh = [int(i) for i in report]
        increasing = bruh[0] < bruh[1]
        ok_boomer = True

        for i, ok in enumerate(bruh):
            if i == len(bruh) - 1:
                break

            if increasing:
                if ok >= bruh[i + 1]:
                    ok_boomer = False
                    break
            else:
                if ok <= bruh[i + 1]:
                    ok_boomer = False
                    break

            if abs(ok - bruh[i + 1]) == 0 or abs(ok - bruh[i + 1]) > 3:
                ok_boomer = False
                break
        if ok_boomer:
            safe += 1
        else:
            herm = False
            for n, m in enumerate(bruh):
                new_list = bruh[:n] + bruh[n + 1:]
                increasing = new_list[0] < new_list[1]
                ok_boomer = True
                for i, ok in enumerate(new_list):
                    if i == len(new_list) - 1:
                        break

                    if increasing:
                        if ok >= new_list[i + 1]:
                            ok_boomer = False
                            break
                    else:
                        if ok <= new_list[i + 1]:
                            ok_boomer = False
                            break

                    if abs(ok - new_list[i + 1]) == 0 or abs(ok - new_list[i + 1]) > 3:
                        ok_boomer = False
                        break
                if ok_boomer:
                    herm = True
            if herm:
                safe += 1
    print(safe)


if __name__ == "__main__":
    sol2()
