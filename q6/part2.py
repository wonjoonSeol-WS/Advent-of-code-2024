filename = "./q6/input"
# filename = "./q6/test"

import sys
from enum import Enum, auto

sys.setrecursionlimit(30000)


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
    start_i, start_j = get_start(grid)
    visited = set()

    def recur(i, j):
        direction = Direction.UP

        while True:
            if (i, j, direction) in visited:
                return True
            if i not in range(m) or j not in range(n) or grid[i][j] == "#":
                break
            visited.add((i, j, direction))

            match direction:
                case Direction.UP:
                    if i - 1 >= 0 and grid[i - 1][j] == "#":
                        direction = Direction.RIGHT
                    else:
                        i -= 1
                case Direction.DOWN:
                    if i + 1 < m and grid[i + 1][j] == "#":
                        direction = Direction.LEFT
                    else:
                        i += 1
                case Direction.LEFT:
                    if j - 1 >= 0 and grid[i][j - 1] == "#":
                        direction = Direction.UP
                    else:
                        j -= 1
                case Direction.RIGHT:
                    if j + 1 < n and grid[i][j + 1] == "#":
                        direction = Direction.DOWN
                    else:
                        j += 1
        return False

    recur(start_i, start_j)
    original_path = visited
    # print(original_path, len(original_path))

    visited = set()
    solution = set()

    for i, j, direction in original_path:
        # if grid[i][j] == "#" or grid[i][j] == "^":
        # continue

        if direction == Direction.UP:
            x = i - 1
            y = j
        elif direction == Direction.DOWN:
            x = i + 1
            y = j
        elif direction == Direction.LEFT:
            x = i
            y = j - 1
        else:
            x = i
            y = j + 1

        if x not in range(m) or y not in range(n) or grid[x][y] == "#" or grid[x][y] == "^" or (x, y) in solution:
            continue
        grid[x][y] = "#"

        visited = set()
        # if recur(i, j, direction):    # 순서 중요 겹치는 부분
        if recur(start_i, start_j):
            solution.add((x, y))
            # res += 1
        grid[x][y] = "."
    print(solution)
    return len(solution)


grid = []
with open(filename, "r") as f:
    while line := f.readline().strip():
        row = []
        for char in line:
            row.append(char)
        grid.append(row)
    print(count(grid))


# it may be passed after wall is placed!
# if (i + 1, j, Direction.UP) in original_path:
#     start_i = i + 1
#     start_j = j
#     dir = Direction.UP
# elif (i - 1, j, Direction.DOWN) in original_path:
#     start_i = i - 1
#     start_j = j
#     dir = Direction.DOWN
# elif (i, j + 1, Direction.LEFT) in original_path:
#     start_i = i
#     start_j = j + 1
#     dir = Direction.LEFT
# else:
#     start_i = i
#     start_j = j - 1
#     dir = Direction.RIGHT


# No need for recursion (stack)
# def count(grid):
#     m = len(grid)
#     n = len(grid[0])
#     i, j = get_start(grid)
#     visited = set()

#     def recur(i, j, direction):
#         if (i, j, direction) in visited:
#             return True
#         if i not in range(m) or j not in range(n) or grid[i][j] == "#":
#             return False

#         visited.add((i, j, direction))

#         match direction:
#             case Direction.UP:
#                 if i - 1 >= 0 and grid[i - 1][j] == "#":
#                     return recur(i, j, Direction.RIGHT)
#                 return recur(i - 1, j, direction)
#             case Direction.DOWN:
#                 if i + 1 < m and grid[i + 1][j] == "#":
#                     return recur(i, j, Direction.LEFT)
#                 return recur(i + 1, j, direction)
#             case Direction.LEFT:
#                 if j - 1 >= 0 and grid[i][j - 1] == "#":
#                     return recur(i, j, Direction.UP)
#                 return recur(i, j - 1, direction)
#             case Direction.RIGHT:
#                 if j + 1 < n and grid[i][j + 1] == "#":
#                     return recur(i, j, Direction.DOWN)
#                 return recur(i, j + 1, direction)
