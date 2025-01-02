import re

prog = re.compile(r"mul\((\d+),(\d+)\)|don't\(\)|do\(\)")


def get_mul(filename):
    res = 0
    with open(filename, "r") as f:
        line = f.read().strip()
        # line = re.sub(r"don't\(\).*(?=do\(\)|$)", "", line, flags=re.DOTALL)
        print(line)
        groups = prog.finditer(line)

        is_active = True
        for match in groups:
            if match.group(0) == "do()":
                is_active = True
            elif match.group(0) == "don't()":
                is_active = False
            else:
                if is_active:
                    a, b = match.group(1), match.group(2)
                    res += int(a) * int(b)
    return res


# do_prog = re.compile(r"do(?!n't)")
# dont_prog = re.compile(r"don't")

# def get_mul(filename):
#     res = 0
#     with open(filename, "r") as f:
#         line = f.read().strip()
#         print(line)
#         match = [(i.start(), (i.group(1), i.group(2))) for i in prog.finditer(line)]
#         do_idx = [(i.start(), True) for i in do_prog.finditer(line)]
#         dont_idx = [(i.start(), False) for i in dont_prog.finditer(line)]

#         commands = sorted(do_idx + dont_idx + match)
#         res = 0
#         print(commands)
#         is_count = True
#         for i, val in commands:
#             if val is True:
#                 is_count = True
#             elif val is False:
#                 is_count = False
#             else:
#                 if is_count:
#                     a, b = val
#                     res += int(a) * int(b)
#     return res


if __name__ == "__main__":
    print(get_mul("q3/test"))
    # print(get_mul("q3/input"))
