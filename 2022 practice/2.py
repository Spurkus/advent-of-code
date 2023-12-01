def win(p1, p2):
    match p1:
        case "A":
            if p2 == "X": return 3
            if p2 == "Y": return 6
            if p2 == "Z": return 0
        case "B":
            if p2 == "X": return 0
            if p2 == "Y": return 3
            if p2 == "Z": return 6
        case "C":
            if p2 == "X": return 6
            if p2 == "Y": return 0
            if p2 == "Z": return 3

def bruh(shape):
    match shape:
        case "X": return 1
        case "Y": return 2
        case "Z": return 3
    

with open("2.txt", "r") as file:
    data = [i.replace("\n", "") for i in file.readlines()]

    a, b = data[0].split()
    score = win(a, b) + bruh(b)

    data.pop(0)

    for i in data:
        p1, p2 = i.split()
        score += win(p1, p2) + bruh(p2)

    print(score)