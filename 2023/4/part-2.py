import sys

with open(sys.argv[1], "r") as input_file:
    lines = [line.strip("\n") for line in input_file.readlines()]

MAX_CARD_INDEX = len(lines)
scratchcards = []


def extract_numbers(numbers):
    return set(int(n.strip()) for n in numbers.split(" ") if n.strip())


def extract_card_numbers():
    winning, yours = numbers.split("|")
    return extract_numbers(winning), extract_numbers(yours)


for line in lines:
    numbers = "".join(line.split(":")[1:])
    winning, yours = extract_card_numbers()
    # number of matching number, number of copies of this card
    scratchcards.append((len(winning & yours), 1))

for index, (nb_winning_numbers, nb_copies) in enumerate(scratchcards):
    for _ in range(nb_copies):
        for i in range(1, nb_winning_numbers + 1):
            if index + i < MAX_CARD_INDEX:
                (a, b) = scratchcards[index + i]
                scratchcards[index + i] = a, b + 1


print(sum(y for _, y in scratchcards))