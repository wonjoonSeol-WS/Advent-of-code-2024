import re

pattern = r"mul\((\d+),(\d+)\)"
prog = re.compile(pattern)


def get_mul(filename):
    res = 0
    with open(filename, "r") as f:
        line = f.read().strip()

        match = prog.findall(line)
        # print(match)
        for a, b in match:
            res += int(a) * int(b)
    return res


if __name__ == "__main__":
    print(get_mul("q3/test"))
    print(get_mul("q3/input"))
