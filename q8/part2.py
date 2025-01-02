res = 0
filename = "q8/input"
# filename = "q8/test"

from collections import defaultdict


def count(grid):
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

                delta_x = x - x2
                delta_y = y - y2

                curr_x = x
                curr_y = y
                while curr_x in range(m) and curr_y in range(n):
                    unique_points.add((curr_x, curr_y))
                    curr_x += delta_x
                    curr_y += delta_y

                curr_x = x2
                curr_y = y2
                while curr_x in range(m) and curr_y in range(n):
                    unique_points.add((curr_x, curr_y))
                    curr_x -= delta_x
                    curr_y -= delta_y
    return len(unique_points)


grid = []

with open(filename) as f:
    while line := f.readline().strip():
        row = []
        for i, char in enumerate(line):
            row.append(char)
        grid.append(row)

    print(count(grid))
