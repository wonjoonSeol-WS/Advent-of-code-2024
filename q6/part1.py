filename = "./q6/input"
# filename = "./q6/test"

import sys
from enum import Enum, auto


class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()


def get_start(grid):
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "^":
                return i, j


def count(grid):
    m = len(grid)
    n = len(grid[0])
    visited = set()
    i, j = get_start(grid)
    direction = Direction.UP

    while True:
        if i not in range(m) or j not in range(n) or grid[i][j] == "#":
            break

        visited.add((i, j))
        match direction:
            case Direction.UP:
                if i - 1 >= 0 and grid[i - 1][j] == "#":
                    direction = Direction.RIGHT
                else:
                    i = i - 1
            case Direction.DOWN:
                if i + 1 < m and grid[i + 1][j] == "#":
                    direction = Direction.LEFT
                else:
                    i = i + 1
            case Direction.LEFT:
                if j - 1 >= 0 and grid[i][j - 1] == "#":
                    direction = Direction.UP
                else:
                    j = j - 1
            case Direction.RIGHT:
                if j + 1 < n and grid[i][j + 1] == "#":
                    direction = Direction.DOWN
                else:
                    j = j + 1

    # for i in range(m):
    #     for j in range(n):
    #         if (i, j) in visited:
    #             grid[i][j] = "x"
    # print(grid)
    return len(visited)


grid = []
with open(filename, "r") as f:
    while line := f.readline().strip():
        row = []
        for char in line:
            row.append(char)
        grid.append(row)
    print(count(grid))
