import sys
import re
from dataclasses import dataclass

rgb_limits = [12, 13, 14]
games = []
num_color_regex = re.compile(r"(?P<num>\d+)\s+(?P<color>\w)")


@dataclass
class Game:
    id: int
    max_rgb: list[int]
    line: str
    is_possible: bool


def color_draw_to_num_index(color_draw):
    index, num = 0, 0
    match = num_color_regex.match(color_draw)
    if match:
        (num, col) = match.groups()
        index = 0
        if col == "g":
            index = 1
        if col == "b":
            index = 2
    return index, int(num)


def parse_game_round(round_to_parse):
    default_draw = [0, 0, 0]
    for color_draw in round_to_parse.split(","):
        index, num = color_draw_to_num_index(color_draw.strip())
        default_draw[index] = num
    return default_draw


def line_to_game(line):
    line_split = line.find(":")
    game_id = int(line[line.find(" ") + 1: line_split])
    max_rgb = [0, 0, 0]
    for r in line[line_split + 1:].split(";"):
        for color_draw in r.split(","):
            index, num = color_draw_to_num_index(color_draw.strip())
            max_rgb[index] = max(max_rgb[index], num)
    is_possible = all(a <= b for a, b in zip(max_rgb, rgb_limits))
    return Game(id=game_id, max_rgb=max_rgb, line=line, is_possible=is_possible)


with open(sys.argv[1], "r") as input_file:
    for line in input_file.readlines():
        games.append(line_to_game(line.strip("\n")))

print("\n".join(f"{g.id}: {g.max_rgb}: {g.is_possible}" for g in games))

possible_games = filter(lambda g: g.is_possible, games)

print(sum(g.id for g in possible_games))
