import heapq

DIRECTIONS = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}
ROTATE = 1000
STEP = 1


class Node:

    def __init__(self, d, i, j, parent, cost):
        self.d = d
        self.i = i
        self.j = j
        self.parent = parent
        self.cost = cost

    def get_position(self):
        return self.d, self.i, self.j

    def get_parent(self):
        return self.parent

    def get_cost(self):
        return self.cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.cost == other.cost


def sol1(nonono, deer, goal):
    # UCS algorithm
    frontier = []
    heapq.heappush(frontier, Node(deer[0], deer[1], deer[2], None, 0))
    explored = set()

    while frontier:
        current = heapq.heappop(frontier)
        d, i, j = current.get_position()

        if (i, j) == goal:
            print(current.get_cost(), current.get_position())

        if (d, i, j) in explored:
            continue
        explored.add((d, i, j))

        forward_i, forward_j = i + DIRECTIONS[d][0], j + DIRECTIONS[d][1]
        if (forward_i, forward_j) not in nonono and (d, forward_i, forward_j) not in explored:
            heapq.heappush(frontier,
                           Node(d, forward_i, forward_j, current,
                                current.get_cost() + STEP))

        for dir in DIRECTIONS:
            if dir != d and (dir, i, j) not in explored and (i + DIRECTIONS[dir][0],
                                                             j + DIRECTIONS[dir][1]) not in nonono:
                heapq.heappush(frontier, Node(dir, i, j, current, current.get_cost() + ROTATE))
    return -1, None


def sol2(nonono, deer, goal):
    # UCS algorithm
    frontier = []
    heapq.heappush(frontier, Node(deer[0], deer[1], deer[2], None, 0))
    explored = {}
    yea = set()

    while frontier:
        current = heapq.heappop(frontier)
        d, i, j = current.get_position()

        if (i, j) == goal and current.get_cost() == 94444:
            yay = current
            while yay:
                _, x, y = yay.get_position()
                yea.add((x, y))
                yay = yay.get_parent()

        if (d, i, j) in explored and explored[(d, i, j)] < current.get_cost():
            continue

        explored[(d, i, j)] = current.get_cost()

        forward_i, forward_j = i + DIRECTIONS[d][0], j + DIRECTIONS[d][1]
        if (forward_i, forward_j) not in nonono:
            heapq.heappush(frontier,
                           Node(d, forward_i, forward_j, current,
                                current.get_cost() + STEP))

        for dir in DIRECTIONS:
            if dir != d and (i + DIRECTIONS[dir][0], j + DIRECTIONS[dir][1]) not in nonono:
                heapq.heappush(frontier, Node(dir, i, j, current, current.get_cost() + ROTATE))
    return len(yea)


if __name__ == "__main__":
    with open("day 16.txt", "r") as file:
        data = [i.replace("\n", "") for i in file.readlines()]

    nonono = set()
    deer = (0, 0)
    goal = ("E", 0, 0)
    for i, j in enumerate(data):
        for n, m in enumerate(j):
            if m == "#":
                nonono.add((i, n))
            elif m == "S":
                deer = ("E", i, n)
            elif m == "E":
                goal = (i, n)

    cost, current = sol1(nonono, deer, goal)
    print(cost)
    print(sol2(nonono, deer, goal))
