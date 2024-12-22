def sol1(secret_numbers):
    yea = 0
    for num in secret_numbers:
        for _ in range(2000):
            num ^= num * 64
            num %= 16777216
            num ^= num // 32
            num %= 16777216
            num ^= num * 2048
            num %= 16777216
        yea += num
    return yea


def sol2(secret_numbers):
    sequences = {}
    for num in secret_numbers:
        all_my_fellas = []
        for _ in range(2000):
            num ^= num * 64
            num %= 16777216
            num ^= num // 32
            num %= 16777216
            num ^= num * 2048
            num %= 16777216
            all_my_fellas.append(num)

        prices = [fella % 10 for fella in all_my_fellas]
        ching = [prices[i] - prices[i - 1] for i in range(1, len(prices))]

        seen = set()

        for i in range(len(ching) - 3):
            sequence = tuple(ching[i:i + 4])
            if sequence not in seen:
                selling_price = prices[i + 4]
                sequences[sequence] = sequences.get(sequence, 0) + selling_price
                seen.add(sequence)

    bruh = max(sequences, key=lambda seq: sequences[seq])
    return sequences[bruh]


if __name__ == "__main__":
    with open("day 22.txt", "r") as file:
        data = [i.replace("\n", "") for i in file.readlines()]
    secret_numbers = [int(i) for i in data]
    print(sol1(secret_numbers))
    print(sol2(secret_numbers))
