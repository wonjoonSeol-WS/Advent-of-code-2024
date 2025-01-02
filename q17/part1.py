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

        # print("i", i, "op", opcode, "operand", combo, "registers", a, b, c)
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
    # print(res, a, b, c)
    return ",".join(map(str, res)), a, b, c


def run_prog2(instructions, a, b, c):
    # print(a, b, c, instructions)
    operands = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: a,
        5: b,
        6: c,
        7: None,
    }

    i = 0
    res = []
    while i < len(instructions):
        opcode = instructions[i]
        operand = instructions[i + 1]
        combo = operands[operand]

        # print("i", i, "op", opcode, "operand", combo, "registers", operands[4], operands[5], operands[6])
        match opcode:
            case 0:
                operands[4] //= 2**combo
            case 1:
                operands[5] ^= operand
            case 2:
                operands[5] = combo % 8
            case 3:
                if operands[4] != 0:
                    i = operand
                    continue
            case 4:
                operands[5] ^= operands[6]
            case 5:
                res.append(combo % 8)
            case 6:
                operands[5] = operands[4] // (2**combo)
            case 7:
                operands[6] = operands[4] // (2**combo)
        i += 2
    return ",".join(map(str, res)), operands[4], operands[5], operands[6]


if __name__ == "__main__":
    instructions, a, b, c = get_input("q17/test")
    res, a, b, c = run_prog(instructions, a, b, c)
    assert res == "4,6,3,5,6,3,5,2,1,0"

    instructions, a, b, c = [5, 0, 5, 1, 5, 4], 10, 0, 0
    res, a, b, c = run_prog(instructions, a, b, c)
    assert res == "0,1,2"

    instructions, a, b, c = [0, 1, 5, 4, 3, 0], 2024, 0, 0
    res, a, b, c = run_prog(instructions, a, b, c)
    assert res == "4,2,5,6,7,7,7,7,3,1,0"
    assert a == 0

    instructions, a, b, c = [2, 6], 0, 0, 9
    res, a, b, c = run_prog(instructions, a, b, c)
    assert b == 1

    instructions, a, b, c = [1, 7], 0, 29, 0
    res, a, b, c = run_prog(instructions, a, b, c)
    assert b == 26

    instructions, a, b, c = [4, 0], 0, 2024, 43690
    res, a, b, c = run_prog(instructions, a, b, c)
    assert b == 44354

    instructions, a, b, c = get_input("q17/input")
    print(run_prog(instructions, a, b, c)[0])
