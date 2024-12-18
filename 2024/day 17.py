def sol1(a, b, c, program):
    i = 0
    output = []
    while i < len(program):
        if i == len(program) - 1:
            break

        will_jump = True
        instruction, operand = program[i], program[i + 1]
        combo_operand = operand

        match operand:
            case 4:
                combo_operand = a
            case 5:
                combo_operand = b
            case 6:
                combo_operand = c

        if instruction == 0:
            a = int(a / (2**combo_operand))
        elif instruction == 1:
            b ^= operand
        elif instruction == 2:
            b = combo_operand % 8
        elif instruction == 3:
            if a != 0:
                i = operand
                will_jump = False
        elif instruction == 4:
            b ^= c
        elif instruction == 5:
            output.append(combo_operand % 8)
        elif instruction == 6:
            b = int(a / (2**combo_operand))
        elif instruction == 7:
            c = int(a / (2**combo_operand))

        if will_jump:
            i += 2
    return output


def sol2(b, c, program):
    to_visit = [(len(program), 0)]
    while to_visit:
        pos, a = to_visit.pop(0)
        for i in range(8):
            n_a = a * 8 + i
            o = list(map(int, sol1(n_a, b, c, program)))
            if o == program[pos - 1:]:
                to_visit.append((pos - 1, n_a))
                if len(o) == len(program):
                    return n_a


if __name__ == "__main__":
    with open("day 17.txt", "r") as file:
        data = [i.replace("\n", "") for i in file.readlines()]

    a = int(data[0].split(":")[1])
    b = int(data[1].split(":")[1])
    c = int(data[2].split(":")[1])

    program = [int(i) for i in data[4].split(": ")[1].split(",")]

    output = sol1(a, b, c, program)
    print(','.join(str(i) for i in output))
    a = sol2(b, c, program)
    print(a, sol1(a, b, c, program))
