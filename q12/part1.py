from collections import defaultdict


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
    regions = defaultdict(list)

    def recur(i, j, char, key):
        if i not in range(m) or j not in range(n) or (i, j) in visited or grid[i][j] != char:
            return
        visited.add((i, j))
        regions[key].append((i, j))

        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            recur(x, y, char, key)

    for i in range(m):
        for j in range(n):
            recur(i, j, grid[i][j], (grid[i][j], (i, j)))
    return regions


def get_perimeter(region, m, n):
    res = 0
    for i, j in region:
        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if x not in range(m) or y not in range(n) or grid[x][y] != grid[i][j]:
                res += 1
    return res


def calculate(grid):
    regions = get_regions(grid)
    m = len(grid)
    n = len(grid[0])

    res = 0
    for region in regions.values():
        area = len(region)
        perimeter = get_perimeter(region, m, n)
        res += area * perimeter
    return res


if __name__ == "__main__":
    grid = get_input("./q12/test")
    print(calculate(grid))

    grid = get_input("./q12/test2")
    print(calculate(grid))

    grid = get_input("./q12/input")
    print(calculate(grid))
