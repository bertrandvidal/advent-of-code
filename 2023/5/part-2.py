import math
import sys

with open(sys.argv[1], "r") as input_file:
    line = [line.strip("\n") for line in input_file.readlines()]

seeds = [int(x) for x in line[0].split(":")[1].split(" ") if x]

maps = []
current_map = []
map_name = None

for line in line[1:]:
    if not line.strip() or "map" in line:
        if "map" in line:
            map_name = line
        if current_map:
            maps.append((map_name, current_map))
        current_map = []
        continue
    map_entry = [int(x) for x in line.split(" ")]
    # source/destination are flipped here to prevent confusion down the line
    destination_entry = (map_entry[0], map_entry[0] + map_entry[2])
    source_entry = (map_entry[1], map_entry[1] + map_entry[2])
    current_map.append((source_entry, destination_entry))

# map is only added when we encounter the next one so the last one is never added, add it "manually"
maps.append((map_name, current_map))


def source_range(entry):
    return entry[0][0], entry[0][1]


def destination_range(entry):
    return entry[1][0], entry[1][1]


assert source_range(((50, 52), (98, 100))) == (50, 52)
assert destination_range(((50, 52), (98, 100))) == (98, 100)


def source_to_dest(index, entry):
    src = source_range(entry)
    dst = destination_range(entry)
    if src[0] <= index < src[1]:
        return dst[0] + index - src[0]
    if index >= src[1]:
        return src[0] + index - src[1]
    return index


assert source_to_dest(0, ((50, 98), (52, 100))) == 0
assert source_to_dest(50, ((50, 98), (52, 100))) == 52
assert source_to_dest(51, ((50, 98), (52, 100))) == 53
assert source_to_dest(52, ((50, 98), (52, 100))) == 54
assert source_to_dest(98, ((50, 98), (52, 100))) == 50, source_to_dest(98, ((50, 98), (52, 100)))
assert source_to_dest(99, ((50, 98), (52, 100))) == 51, source_to_dest(99, ((50, 98), (52, 100)))


def seed_to_location(seed, maps):
    current_index = seed
    for map_name, current_map in maps:
        for m in current_map:
            src = source_range(m)
            if src[0] <= current_index < src[1]:
                current_index = source_to_dest(current_index, m)
                break
    return current_index


min_location = math.inf
ranges = [range(x[0], x[0] + x[1]) for x in zip(*(iter(seeds),) * 2)]


def range_is_included(source, dest):
    """Is source fully included in dest"""
    return source[0] >= dest[0] and source[1] <= dest[1]


assert range_is_included((0, 5), (6, 10)) == False
assert range_is_included((5, 10), (0, 15)) == True
assert range_is_included((10, 20), (0, 10)) == False


def range_is_outside(source, dest):
    """Whether source is fully outside dest"""
    return source[1] < dest[0] or source[0] > dest[1]


assert range_is_outside((0, 5), (6, 10)) == True
assert range_is_outside((0, 5), (3, 10)) == False
assert range_is_outside((1, 5), (0, 10)) == False
assert range_is_outside((11, 20), (0, 10)) == True


def split_range(source, dest, transform=lambda x: x):
    """Split source into 2 intervals and applies transform to the part of source that overlaps with dest"""
    s0, s1 = source
    d0, d1 = dest
    if d0 <= s0 <= d1:
        return (s0, d1), (d1, s1)
    if d0 <= s1 <= d1:
        return (d0, s1), (s1, d1)


assert split_range((0, 5), (3, 10)) == ((0, 3), (3, 5)), split_range((0, 5), (3, 10))



assert split_range((0, 5), (3, 10), lambda x: x * 2) == ((0, 3), (6, 10)), split_range((0, 5), (3, 10), lambda x: x * 2)
assert split_range((5, 10), (3, 8), lambda x: x) == ((5, 8), (8, 10)), split_range((5, 10), (3, 8), lambda x: x)
assert split_range((5, 10), (3, 8), lambda x: x * 2) == ((10, 16), (8, 10)), split_range((5, 10), (3, 8), lambda x: x * 2)

# lower than 670,311,579
print(maps)
