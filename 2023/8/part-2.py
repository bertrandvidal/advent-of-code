import re
import sys
import math

line_regex = re.compile(r'(?P<node>[A-Z]{3}) = \((?P<L>[A-Z]{3}), (?P<R>[A-Z]{3})\)')

with open(sys.argv[1], "r") as input_file:
    lines = [line.strip("\n") for line in input_file.readlines()]

instructions = [x for x in lines[0]]

start_nodes = []
nodes = {}
start_node, end_node = None, None

for line in lines[1:]:
    match = line_regex.match(line)
    if match:
        groups = match.groups()
        nodes[groups[0]] = {"L": groups[1], "R": groups[2]}
        if groups[0].endswith("A"):
            start_nodes.append(groups[0])

iterations = []

for current_node in start_nodes:
    iteration = 0
    while not current_node.endswith("Z"):
        for step in instructions:
            current_node = nodes[current_node][step]
            iteration += 1
    iterations.append(iteration)

print(f"total {math.lcm(*iterations)=}")