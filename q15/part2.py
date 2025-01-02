from collections import deque, defaultdict


def get_start(grid):
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "@":
                return i, j
    return -1, -1


def move_robot(grid, i, j, dx, dy):
    m = len(grid)
    n = len(grid[0])
    start_i, start_j = i, j

    def bfs(q, dx, dy):
        locations = set()
        while q:
            len_q = len(q)
            for _ in range(len_q):
                i, j = q.popleft()

                locations.add((i, j))
                if i + dx not in range(m) or j + dy not in range(n) or grid[i + dx][j + dy] == "#":
                    return start_i, start_j

                char = grid[i + dx][j + dy]
                if char == "." or (i + dx, j + dy) in locations:
                    continue
                if char == "[":
                    q.append((i + dx, j + dy))
                    q.append((i + dx, j + dy + 1))
                elif char == "]":
                    q.append((i + dx, j + dy))
                    q.append((i + dx, j + dy - 1))
                else:
                    raise NotImplementedError

        cache = defaultdict(dict)
        for i, j in locations:
            cache[i][j] = grid[i][j]
            grid[i][j] = "."

        for i, j in locations:
            grid[i + dx][j + dy] = cache[i][j]

        grid[start_i][start_j] = "."
        # grid[start_i + dx][start_j + dy] = "@"
        return start_i + dx, start_j + dy

    q = deque([(i, j)])
    return bfs(q, dx, dy)


def score(grid):
    m = len(grid)
    n = len(grid[0])
    score = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "[":
                score += 100 * i + j
    return score


def solve(grid, moves):
    i, j = get_start(grid)
    # print_grid(grid)
    for move in moves:
        # print(i, j, move)
        match move:
            case "^":
                i, j = move_robot(grid, i, j, -1, 0)
            case ">":
                i, j = move_robot(grid, i, j, 0, 1)
            case "<":
                i, j = move_robot(grid, i, j, 0, -1)
            case "v":
                i, j = move_robot(grid, i, j, +1, 0)
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
                if char == "O":
                    row.append("[")
                    row.append("]")
                elif char == ".":
                    row.append(char)
                    row.append(char)
                elif char == "#":
                    row.append("#")
                    row.append("#")
                else:
                    row.append("@")
                    row.append(".")
            grid.append(row)

        for line in part2.strip().split("\n"):
            for char in line:
                moves.append(char)
    return grid, moves


if __name__ == "__main__":
    grid, moves = get_input("q15/test")
    print(solve(grid, moves))
    grid, moves = get_input("q15/input")
    print(solve(grid, moves))
