from collections import deque
import heapq


def get_input(filename):
    grid = []
    with open(filename, "r") as f:
        while line := f.readline().strip():
            row = []
            for char in line:
                row.append(char)
            grid.append(row)
    return grid


def get_start(grid):
    m = len(grid)
    n = len(grid[0])

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "S":
                return i, j
    return -1, -1


def get_end(grid):
    m = len(grid)
    n = len(grid[0])

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "E":
                return i, j
    return -1, -1


def get_next_direction(dx, dy):
    if dx != 0:
        return [(0, 1), (0, -1)]
    return [(1, 0), (-1, 0)]


def get_other_direction(dx, dy):
    return -1 * dx, -1 * dy


def solve(grid):
    m = len(grid)
    n = len(grid[0])

    start_i, start_j = get_start(grid)
    goal_i, goal_j = get_end(grid)
    # print(start_i, start_j)
    # print(goal_i, goal_j)
    visited = set()

    def shortest_path(i, j, goal_i, goal_j):
        min_heap = [(0, i, j, 0, 1)]  # score, i, j, di, dj

        while min_heap:
            score, i, j, dx, dy = heapq.heappop(min_heap)

            if i == goal_i and j == goal_j:
                return score

            if (
                i + dx in range(m)
                and j + dy in range(n)
                and grid[i + dx][j + dy] != "#"
                and (i + dx, j + dy) not in visited
            ):
                heapq.heappush(min_heap, (score + 1, i + dx, j + dy, dx, dy))

            # print(score, "curr", i, j, "dir", dx, dy)
            if (i, j) not in visited:
                for new_dx, new_dy in get_next_direction(dx, dy):
                    heapq.heappush(min_heap, (score + 1000, i, j, new_dx, new_dy))
                # start does not need to go west
                # new_dx, new_dy = get_other_direction(dx, dy)
                # heapq.heappush(min_heap, (score + 2000, i, j, new_dx, new_dy))

            visited.add((i, j))
        return -1

    return shortest_path(start_i, start_j, goal_i, goal_j)


if __name__ == "__main__":
    grid = get_input("q16/test")
    print(solve(grid))
    # get_input("q16/test2")
    grid = get_input("q16/input")
    print(solve(grid))
