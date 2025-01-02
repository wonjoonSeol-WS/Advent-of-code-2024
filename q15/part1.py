def get_start(grid):
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "@":
                return i, j
    return -1, -1


def push(grid, i, j, dx, dy):
    m = len(grid)
    n = len(grid[0])
    x = i + dx
    y = j + dy
    while x in range(m) and y in range(n) and grid[x][y] == "O":
        x += dx
        y += dy

    if x in range(m) and y in range(n):
        if grid[x][y] == "#":
            return i, j
        if grid[x][y] == ".":
            grid[x][y], grid[i + dx][j + dy] = grid[i + dx][j + dy], grid[x][y]
            grid[i + dx][j + dy], grid[i][j] = grid[i][j], grid[i + dx][j + dy]
            return i + dx, j + dy
    return i, j


def score(grid):
    m = len(grid)
    n = len(grid[0])
    score = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "O":
                score += 100 * i + j
    return score


def solve(grid, moves):
    i, j = get_start(grid)
    # print_grid(grid)
    for move in moves:
        # print(i, j, move)
        match move:
            case "^":
                i, j = push(grid, i, j, -1, 0)
            case ">":
                i, j = push(grid, i, j, 0, 1)
            case "<":
                i, j = push(grid, i, j, 0, -1)
            case "v":
                i, j = push(grid, i, j, +1, 0)
            case _:
                raise NotImplementedError
        # print_grid(grid)
    return score(grid)


def print_grid(grid):
    m = len(grid)

    for i in range(m):
        print(grid[i])


def get_input(filename):
    grid = []
    moves = []
    with open(filename, "r") as f:
        part1, part2 = f.read().strip().split("\n\n")

        for line in part1.strip().split("\n"):
            row = []
            for char in line:
                row.append(char)
            grid.append(row)

        for line in part2.strip().split("\n"):
            for char in line:
                moves.append(char)
    return grid, moves


if __name__ == "__main__":
    # grid, moves = get_input("q15/test")
    # print(solve(grid, moves))

    grid, moves = get_input("q15/input")
    print(solve(grid, moves))
