import string
import sys

SYMBOLS = string.punctuation.replace(".", "")

with open(sys.argv[1], "r") as input_file:
    lines = [line.strip("\n") for line in input_file.readlines()]


def adjacent_characters(x, y, schematic):
    for x_index in range(x - 1, x + 1 + 1):
        for y_index in range(y - 1, y + 1 + 1):
            if (len(schematic) > x_index >= 0
                    and 0 <= y_index < len(schematic[x_index])):
                yield schematic[x_index][y_index]


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


def get_part_numbers_from_schematic(schematic):
    part_numbers = []
    last_value_added = None
    for x, line in enumerate(schematic):
        new_line = []
        for y, char in enumerate(line):
            if char.isdigit() and any(c in SYMBOLS for c in adjacent_characters(x, y, schematic)):
                new_line.append(char)
                current_value = int(find_surrounding_digits(char, schematic[x], y))
                if current_value != last_value_added:
                    part_numbers.append(current_value)
                    last_value_added = current_value
            else:
                last_value_added = None
                new_line.append(".")
        print(new_line)
    return part_numbers


print(sum(get_part_numbers_from_schematic(lines)))
