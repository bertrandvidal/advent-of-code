import re
import string
import sys

calibrations = []

written_to_digits = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9∞e"
}

regex = re.compile("|".join(written_to_digits.keys()))


def replace_written_digits_with_numbers(line_with_written_digits):
    match = regex.search(line_with_written_digits)
    while match:
        line_with_written_digits = line_with_written_digits.replace(match.group(), written_to_digits[match.group()], 1)
        match = regex.search(line_with_written_digits)
    return line_with_written_digits


def find_first_digit_in_line(line_looking_for_digits):
    for c in line_looking_for_digits:
        if c.isdigit():
            return c


def find_last_digit_in_line(line_looking_for_digits):
    return find_first_digit_in_line(line_looking_for_digits[::-1])


with open(sys.argv[1], "r") as input_file:
    for original_line in input_file.readlines():
        original_line = original_line.strip("\n")
        line = replace_written_digits_with_numbers(original_line)
        calibration = find_first_digit_in_line(line) + find_last_digit_in_line(line)
        print(f"{original_line=} {line=} {calibration=}")
        calibrations.append(int(calibration))

print(sum(calibrations))
