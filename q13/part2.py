import re

button_pattern = r"Button \w: X\+(\d+), Y\+(\d+)"
prize_pattern = r"Prize: X=(\d+), Y=(\d+)"
button_prog = re.compile(button_pattern)
prize_prog = re.compile(prize_pattern)


def brute(a_x, a_y, b_x, b_y, goal_x, goal_y):
    for a in range(101):
        for b in range(101):
            if goal_x == a_x * a + b_x * b and goal_y == b_y * b + a_y * a:
                return a, b
    return None, None


def solve(a1, a2, b1, b2, c1, c2):
    x = (c1 * b2 - b1 * c2) / (a1 * b2 - b1 * a2)
    y = (c2 * a1 - a2 * c1) / (a1 * b2 - b1 * a2)
    if int(x) != x or int(y) != y:
        return None, None

    # if a > 100 or b > 100:
    # return None, None
    return x, y


def calculate_point(a, b):
    if not a or not b:
        return 0
    return 3 * a + b


def process(filename):
    with open(filename, "r") as f:
        lines = f.read().strip()
        games = lines.split("\n\n")
        res = 0
        for game in games:
            arr = game.split("\n")
            # print(arr)
            a1, a2 = map(int, button_prog.match(arr[0]).groups())
            b1, b2 = map(int, button_prog.match(arr[1]).groups())
            c1, c2 = map(int, prize_prog.match(arr[2]).groups())
            c1 += 10000000000000
            c2 += 10000000000000
            a, b = solve(a1, a2, b1, b2, c1, c2)
            # if a:
            print(a, b)
            res += calculate_point(a, b)
        print(res)


if __name__ == "__main__":
    # process("q13/test2")
    process("q13/input")
