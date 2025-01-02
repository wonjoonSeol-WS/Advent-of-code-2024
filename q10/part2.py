def get_input(filename):
    with open(filename, "r") as f:
        grid = []
        while line := f.readline().strip():
            row = []
            for char in line:
                row.append(int(char))
            grid.append(row)
    return grid


def get_start_pos(grid):
    m = len(grid)
    n = len(grid)

    start = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                start.append((i, j))

    return start


def calculate_scores(grid):
    m = len(grid)
    n = len(grid[0])

    start = get_start_pos(grid)
    cache = {}

    def recur(i, j, prev):
        if i not in range(m) or j not in range(n) or grid[i][j] != prev + 1:
            return 0

        if (i, j) in cache:
            return cache[(i, j)]

        if grid[i][j] == 9:
            return 1

        val = grid[i][j]
        res = 0
        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            res += recur(x, y, val)

        cache[(i, j)] = res
        return res

    res = 0
    for i, j in start:
        # print(recur(i, j, - 1))
        res += recur(i, j, -1)
    return res


if __name__ == "__main__":
    grid = get_input("./q10/test")
    assert calculate_scores(grid) == 81

    grid = get_input("./q10/input")
    print(calculate_scores(grid))
