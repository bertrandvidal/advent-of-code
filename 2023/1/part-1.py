import sys

calibrations = []

def find_first_digit_in_line(line):
    for c in line:
        if c.isdigit():
            return c

def find_last_digit_in_line(line):
    for c in line[::-1]:
        if c.isdigit():
            return c

with open(sys.argv[1], "r") as input_file:
    for line in input_file.readlines():
        calibration = find_first_digit_in_line(line) + find_last_digit_in_line(line)
        calibrations.append(int(calibration))

print(calibrations)
print(sum(calibrations))
