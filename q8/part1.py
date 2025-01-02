res = 0
filename = "q8/input"
# filename = "q8/test"

from collections import defaultdict


def count(grid):
    print(grid)
    m = len(grid)
    n = len(grid[0])

    charmap = defaultdict(list)
    unique_points = set()

    for i in range(m):
        for j in range(n):
            if grid[i][j] == ".":
                continue
            else:
                charmap[grid[i][j]].append((i, j))

    for _, val in charmap.items():
        for i in range(len(val)):
            for j in range(i + 1, len(val)):
                x, y = val[i]
                x2, y2 = val[j]

                if x + x - x2 in range(m) and y + y - y2 in range(n):
                    unique_points.add((x + x - x2, y + y - y2))

                if x2 + x2 - x in range(m) and y2 + y2 - y in range(n):
                    unique_points.add((x2 + x2 - x, y2 + y2 - y))

    return len(unique_points)


grid = []

with open(filename) as f:
    while line := f.readline().strip():
        row = []
        for i, char in enumerate(line):
            row.append(char)
        grid.append(row)

    print(count(grid))
