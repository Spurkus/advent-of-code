from math import ceil, log10

with open("day 7.txt", "r") as file:
    data = [(int(n[0]), tuple([int(m)
                               for m in n[1].split()]))
            for n in [i.replace("\n", "").split(":") for i in file.readlines()]]


def possible1(lhs, rhs):
    n = len(rhs)

    def recursion_baby(ok, interesting):
        if ok == n:
            return interesting == lhs

        nextjs = rhs[ok]
        return (recursion_baby(ok + 1, interesting + nextjs) or
                recursion_baby(ok + 1, interesting * nextjs))

    return recursion_baby(1, rhs[0])


def possible2(lhs, rhs):
    n = len(rhs)

    def recursion_baby(ok, interesting):
        if ok == n:
            return interesting == lhs

        nextjs = rhs[ok]
        return (recursion_baby(ok + 1, interesting + nextjs) or
                recursion_baby(ok + 1, interesting * nextjs) or
                recursion_baby(ok + 1, interesting // nextjs) or
                recursion_baby(ok + 1, interesting * 10**ceil(log10(nextjs + 1)) + nextjs))

    return recursion_baby(1, rhs[0])


def sol1():
    total = 0
    for lhs, rhs in data:
        if possible1(lhs, rhs):
            total += lhs
    return total


def sol2():
    total = 0
    for lhs, rhs in data:
        if possible2(lhs, rhs):
            total += lhs
    return total


if __name__ == "__main__":
    print(sol1())
    print(sol2())
