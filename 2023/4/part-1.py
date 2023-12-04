import sys

with open(sys.argv[1], "r") as input_file:
    lines = [line.strip("\n") for line in input_file.readlines()]

scratchcards = []


def extract_numbers(numbers):
    return set(int(n.strip()) for n in numbers.split(" ") if n.strip())


def extract_card_numbers():
    winning, yours = numbers.split("|")
    return extract_numbers(winning), extract_numbers(yours)


for line in lines:
    numbers = "".join(line.split(":")[1:])
    scratchcards.append(extract_card_numbers())

print(sum(pow(2, len(i) - 1) for i in [w & y for w, y in scratchcards] if i))
