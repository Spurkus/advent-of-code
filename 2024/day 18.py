import heapq

MOVEMENTS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def sol1(coords):
    start = (0, 0)
    goal = (70, 70)

    frontier = []
    heapq.heappush(frontier, (0, start))
    explored = set()

    while frontier:
        current_cost, current = heapq.heappop(frontier)
        if current == goal:
            return current_cost
        if current in explored:
            continue
        explored.add(current)

        for move in MOVEMENTS:
            new = (current[0] + move[0], current[1] + move[1])
            if new not in coords and new not in explored and 0 <= new[0] <= 70 and 0 <= new[1] <= 70:
                heapq.heappush(frontier, (current_cost + 1, new))
    return False


if __name__ == "__main__":
    with open("day 18.txt", "r") as file:
        data = [i.replace("\n", "") for i in file.readlines()]

    yes = []
    uh = []
    for j, i in enumerate(data):
        n = i.split(",")
        if j <= 1024:
            yes.append((int(n[0]), int(n[1])))
        else:
            uh.append((int(n[0]), int(n[1])))

    print(sol1(yes))

    # Sol 2
    for j, i in enumerate(uh):
        yes.append(i)
        ok = sol1(yes)
        if not ok:
            print(i)
            break
