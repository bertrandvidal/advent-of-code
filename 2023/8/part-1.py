import pprint
import re
import sys

line_regex = re.compile(r'(?P<node>[A-Z]{3}) = \((?P<L>[A-Z]{3}), (?P<R>[A-Z]{3})\)')

with open(sys.argv[1], "r") as input_file:
    lines = [line.strip("\n") for line in input_file.readlines()]

instructions = [x for x in lines[0]]

nodes = {}
start_node, end_node = None, None

for line in lines[1:]:
    match = line_regex.match(line)
    if match:
        groups = match.groups()
        nodes[groups[0]] = {"L": groups[1], "R": groups[2]}
        if not start_node:
            start_node = groups[0]

end_node = "ZZZ"
current_node = "AAA"
iterations = 0
print(f"{start_node=} / {end_node=} / {nodes=}")

while current_node != end_node:
    for step in instructions:
        if iterations % 10_000_000 == 0:
            print(f"{iterations=} / {current_node=}")
        current_node = nodes[current_node][step]
        iterations += 1
print(f"total {iterations=}")