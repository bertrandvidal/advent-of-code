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

def replace_written_digits_with_numbers(line):
    for k,v in sorted(written_to_digits.items()):
        line = line.replace(k,v,1)
    return line

def find_first_digit_in_line(line):
    for c in line:
        if c.isdigit():
            return c

def find_last_digit_in_line(line):
    for c in line[::-1]:
        if c.isdigit():
            return c

with open(sys.argv[1], "r") as input_file:
    for original_line in input_file.readlines():
        original_line = original_line.strip("\n")
        line = replace_written_digits_with_numbers(original_line)
        calibration = find_first_digit_in_line(line) + find_last_digit_in_line(line)
        print(f"{original_line=} {line=} {calibration=}")
        calibrations.append(int(calibration))

print(sum(calibrations))
