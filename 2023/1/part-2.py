import re
import string
import sys

calibrations = []

written_to_digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
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


assert replace_written_digits_with_numbers("onetwothreefourfivesixseveneightnine") == "123456789"
assert replace_written_digits_with_numbers("nineeightsevensixfivefourthreetwoone") == "123456789"[::-1]
assert replace_written_digits_with_numbers("onetwonethree") == "12ne3"
assert replace_written_digits_with_numbers("oneightnine") == "1ight9"
assert replace_written_digits_with_numbers("nineightnine") == "9ight9"
assert replace_written_digits_with_numbers("nineightnineight") == "9ight9ight"
assert replace_written_digits_with_numbers("nineightnineightthree") == "9ight9ight3"
assert replace_written_digits_with_numbers("sevenine") == "7ine"
assert replace_written_digits_with_numbers("threeight") == "3ight"
assert replace_written_digits_with_numbers("one2one") == "121"
assert replace_written_digits_with_numbers("one2one5") == "1215"
assert replace_written_digits_with_numbers("one9mpggcblrpstzpvfffivelkrqvkvkkhtzseven") == "19mpggcblrpstzpvff5lkrqvkvkkhtz7"
assert find_first_digit_in_line(string.ascii_lowercase + "1" + string.ascii_lowercase) == "1"
assert find_first_digit_in_line(string.ascii_lowercase + "1") == "1"
assert find_first_digit_in_line("1" + string.ascii_lowercase) == "1"
assert find_last_digit_in_line(string.ascii_lowercase + "1" + string.ascii_lowercase) == "1"
assert find_last_digit_in_line(string.ascii_lowercase + "1") == "1"
assert find_last_digit_in_line("1" + string.ascii_lowercase) == "1"

with open(sys.argv[1], "r") as input_file:
    for original_line in input_file.readlines():
        original_line = original_line.strip("\n")
        line = replace_written_digits_with_numbers(original_line)
        calibration = find_first_digit_in_line(line) + find_last_digit_in_line(line)
        print(f"{original_line=} {line=} {calibration=}")
        calibrations.append(int(calibration))

print(sum(calibrations))
