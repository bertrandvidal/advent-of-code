import sys
import pprint

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
        print(f"{map_name} => {current_index}")
    print("\n\n")
    return current_index


print(min(seed_to_location(seed, maps) for seed in seeds))
