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
            a_x, a_y = map(int, button_prog.match(arr[0]).groups())
            b_x, b_y = map(int, button_prog.match(arr[1]).groups())
            goal_x, goal_y = map(int, prize_prog.match(arr[2]).groups())
            a, b = brute(a_x, a_y, b_x, b_y, goal_x, goal_y)
            res += calculate_point(a, b)
        print(res)


if __name__ == "__main__":
    process("q13/test")
    process("q13/input")
