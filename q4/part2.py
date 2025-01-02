TARGET = "XMAS"


def get_input(filename):
    grid = []
    with open(filename, "r") as f:
        while line := f.readline().strip():
            row = []
            for char in line:
                row.append(char)
            grid.append(row)
    return grid


expected = {"M", "S"}


def find_words(grid):
    m = len(grid)
    n = len(grid[0])

    def helper(i, j):
        expected = {"M", "S"}
        diag_one = set()
        diag_two = set()
        diag_one.add(grid[i - 1][j - 1])
        diag_one.add(grid[i + 1][j + 1])

        diag_two.add(grid[i - 1][j + 1])
        diag_two.add(grid[i + 1][j - 1])
        # print(diag_one, diag_one == expected, diag_two, diag_two == expected)
        if diag_one == expected and diag_two == expected:
            return 1
        return 0

    ret = 0
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            if grid[i][j] != "A":
                continue
            ret += helper(i, j)
    return ret


if __name__ == "__main__":
    grid = get_input("q4/test")
    print(find_words(grid))

    grid = get_input("q4/input")
    print(find_words(grid))
