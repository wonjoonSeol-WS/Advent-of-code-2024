from collections import defaultdict
from enum import Enum, auto


class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()


def get_input(filename):
    grid = []
    with open(filename, "r") as f:
        while line := f.readline().strip():
            row = []
            for char in line:
                row.append(char)
            grid.append(row)
    return grid


def get_regions(grid):
    m = len(grid)
    n = len(grid[0])

    visited = set()
    regions = defaultdict(set)

    def recur(i, j, char, key):
        if i not in range(m) or j not in range(n) or (i, j) in visited or grid[i][j] != char:
            return
        visited.add((i, j))
        regions[key].add((i, j))

        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            recur(x, y, char, key)

    for i in range(m):
        for j in range(n):
            recur(i, j, grid[i][j], (grid[i][j], (i, j)))
    return regions


def get_perimeter(region):
    res = 0
    checked = set()

    for i, j in region:
        for dx, dy, dir in [
            (1, 0, Direction.DOWN),
            (-1, 0, Direction.UP),
            (0, 1, Direction.RIGHT),
            (0, -1, Direction.LEFT),
        ]:
            if (i, j, dir) in checked:
                continue

            if (i + dx, j + dy) not in region:
                res += 1

                if dir in [Direction.UP, Direction.DOWN]:
                    di = 0
                    dj = 1
                else:
                    di = 1
                    dj = 0

                curr_i = i
                curr_j = j
                while (curr_i, curr_j) in region and (
                    curr_i + dx,
                    curr_j + dy,
                ) not in region:
                    checked.add((curr_i, curr_j, dir))
                    curr_i += di
                    curr_j += dj

                curr_i = i
                curr_j = j
                while (curr_i, curr_j) in region and (
                    curr_i + dx,
                    curr_j + dy,
                ) not in region:
                    checked.add((curr_i, curr_j, dir))
                    curr_i -= di
                    curr_j -= dj
    return res


def calculate(grid):
    regions = get_regions(grid)

    res = 0
    for key, region in regions.items():
        area = len(region)
        perimeter = get_perimeter(region)
        print(key, area, perimeter)
        res += area * perimeter
    return res


if __name__ == "__main__":
    grid = get_input("./q12/test")
    print(calculate(grid))

    # grid = get_input("./q12/test2")
    # print(calculate(grid))

    grid = get_input("./q12/input")
    print(calculate(grid))
