import sys

with open(sys.argv[1], "r") as input_file:
    lines = [line.strip("\n") for line in input_file.readlines()]


def adjacent_characters(x, y, schematic):
    for x_index in range(x - 1, x + 1 + 1):
        for y_index in range(y - 1, y + 1 + 1):
            if (len(schematic) > x_index >= 0
                    and 0 <= y_index < len(schematic[x_index])):
                if schematic[x_index][y_index].isdigit():
                    yield x_index, y_index, schematic[x_index][y_index]


def find_surrounding_digits(anchor, x_row, pos_y):
    part_number = anchor
    left_index = pos_y - 1
    while left_index >= 0 and x_row[left_index].isdigit():
        part_number = x_row[left_index] + part_number
        left_index -= 1
    right_index = pos_y + 1
    while right_index < len(x_row) and x_row[right_index].isdigit():
        part_number = part_number + x_row[right_index]
        right_index += 1
    return part_number

from functools import reduce

def main():
    for x, line in enumerate(lines):
        for y, char in enumerate(line):
            if char == "*":
                adjacent_numbers = list(adjacent_characters(x, y, lines))
                if len(adjacent_numbers) >= 2:
                    valid_numbers = set()
                    last_value_added = None
                    for x_index, y_index, value in adjacent_numbers:
                        digits = int(find_surrounding_digits(value, lines[x_index], y_index))
                        valid_numbers.add(digits)
                    if len(valid_numbers) == 2:
                        yield reduce(lambda a, b: a * b, valid_numbers)


print(sum(main()))
