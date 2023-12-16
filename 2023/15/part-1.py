example = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"


def h(s):
    current_value = 0
    for c in s:
        current_value += ord(c)
        current_value *= 17
    return current_value % 256


assert sum(h(x) for x in example.split(",")) == 1320

import sys

with open(sys.argv[1]) as input_file:
    print(sum(h(x) for x in input_file.readline().strip("\n").split(",")))
