import sys
import pprint

area_map = []

start_x, start_y = -1, -1

with open(sys.argv[1], "r") as input_file:
    for y, line in enumerate(input_file.readlines()):
        current_line = []
        for x, char in enumerate(line.strip("\n")):
            current_line.append(char)
            if char == "S":
                start_x, start_y = x, y

        area_map.append(current_line)

print(f"start = {start_x}, {start_y}")
pprint.pp(area_map)

print(f"{area_map[start_x][start_y]=}")

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.


