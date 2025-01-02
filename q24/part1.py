from collections import defaultdict, deque
from time import time


class Connection:
    def __init__(self, a, operator, b):
        self.op = operator
        self.a = a
        self.b = b


def get_input(filename):
    known = {}
    wire_map = {}
    with open(filename) as f:
        lines = f.read().strip()
        part1, part2 = lines.split("\n\n")

        for line in part1.split("\n"):
            name, value = line.split(": ")
            known[name] = int(value)

        for line in part2.split("\n"):
            part1, res = line.split(" -> ")
            a, operator, b = part1.split(" ")
            wire_map[res] = Connection(a, operator, b)

    return known, wire_map


op = {
    "AND": lambda x, y: x & y,
    "OR": lambda x, y: x | y,
    "XOR": lambda x, y: x ^ y,
}


def run_wire(known, wire_map, wire):
    if wire in known:
        return known[wire]

    conn = wire_map[wire]
    known[wire] = op[conn.op](run_wire(known, wire_map, conn.a), run_wire(known, wire_map, conn.b))
    return known[wire]


def solve(known, wire_map):
    res = []
    for wire in sorted(wire_map.keys()):
        if wire.startswith("z"):
            val = run_wire(known, wire_map, wire)
            res.append(val)

    # print(list(reversed(res)))
    res = map(str, reversed(res))
    return int("".join(res), base=2)


if __name__ == "__main__":
    start = time()
    known, wire_map = get_input("q24/input")
    print(solve(known, wire_map))
    print(time() - start)
