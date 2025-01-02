def get_input(filename):
    with open(filename, "r") as f:
        lines = f.read().strip()
        part1, part2 = lines.split("\n\n")
        instructions = []

        registers = part1.split("\n")
        a = int(registers[0].split(":")[1])
        b = int(registers[1].split(":")[1])
        c = int(registers[2].split(":")[1])

        part2 = part2.split(":")[1].strip()

        for char in part2.split(","):
            instructions.append(int(char))

    return instructions, a, b, c


def run_prog(instructions, a, b, c):
    print(a, b, c, instructions)

    def get_combo(operand):
        if operand <= 3:
            return operand
        if operand == 4:
            return a
        if operand == 5:
            return b
        if operand == 6:
            return c
        return -1

    i = 0
    res = []
    while i < len(instructions):
        opcode = instructions[i]
        operand = instructions[i + 1]
        combo = get_combo(operand)

        # print("i", i, "op", opcode, "operand", combo, "registers", operands[4], operands[5], operands[6])
        match opcode:
            case 0:
                a //= 2**combo
            case 1:
                b ^= operand
            case 2:
                b = combo % 8
            case 3:
                if a != 0:
                    i = operand
                    continue
            case 4:
                b ^= c
            case 5:
                res.append(combo % 8)
            case 6:
                b = a // (2**combo)
            case 7:
                c = a // (2**combo)
        i += 2
    print(res, a, b, c)
    return res, a, b, c


"""
Register A: 21539243
Register B: 0
Register C: 0

Program: 2,4,1,3,7,5,1,5,0,3,4,1,5,5,3,0

2,4
    b = a % 8
1,3
    b = b ^ 3
7,5
    c = a // (2 ** b)
1,5
    b = b ^ 5
0,3
    a = a // 8
4,1
    b = b ^ c
5,5
    res.append(b % 8)
3,0
    jump i = 0
"""

"""
a = 0 b = 0 c = 0
b = 3
c = 0
b = 6
a = 0
b = 6
append(6)

a = 16, b = 0, c =0
b = 0
c = 16
b = 21
a = 2
b = 5

a = 2 b = 5 c = 16
b = 2
b = 1
c = 0
b = 4
a = 0
b = 4
append(4)
 -> need to traverse from the back
"""


def input_program(a):
    res = []
    b = 0
    c = 0
    while a > 0:
        b = a % 8  # b is base 8 (mod 8) -> 0 <= b <= 7
        b = b ^ 3  # 011 -> [2, 1, 0, 7, 6, 5, 4] num change -> still 0 <= b <= 7
        # c = a // (2 ** b)
        c = a >> b  # top x bits - b bits (base 8).
        b ^= 5  # still 0 <= b <= 7
        # a //= 8 # a divided by 8 each iteration
        a = a >> 3
        b ^= c  # top (x - b) bits -> decreasing each iteration?
        res.append(b % 8)  # the program is always in base 8
    # print(res)
    return res


def find_a(instructions):
    # print("to match", instructions)
    candidates = [0]
    for i in range(len(instructions)):
        next_candidates = []
        for cand in candidates:
            for curr in range(8):
                temp = cand * 8 + curr
                if input_program(temp) == instructions[-i - 1 :]:
                    next_candidates.append(temp)
        candidates = next_candidates
        # print(candidates)
    return min(candidates)


if __name__ == "__main__":
    # instructions, a, b, c = get_input("q17/input")
    # print(input_program(a))   # a = 21539243

    original = [2, 4, 1, 3, 7, 5, 1, 5, 0, 3, 4, 1, 5, 5, 3, 0]  # len 16
    # 6, 49, [393, 397, 425, 429, 430]
    a = find_a(original)
    assert input_program(a) == original
    print("ans", a, input_program(a))
