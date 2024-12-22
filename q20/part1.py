import heapq
from collections import defaultdict
from time import time


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


def djikstra(grid, visited, start_i, start_j):
    min_heap = [(0, start_i, start_j)]

    while min_heap:
        cost, i, j = heapq.heappop(min_heap)

        if (i, j) in visited:
            continue

        visited[(i, j)] = cost
        if grid[i][j] == "E":
            return cost

        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if grid[x][y] != "#":
                heapq.heappush(min_heap, (cost + 1, x, y))
    return float("inf")


def solve(grid, saved):
    m = len(grid)
    n = len(grid[0])
    start_i, start_j = get_start(grid)
    res = defaultdict(int)
    visited = {}
    djikstra(grid, visited, start_i, start_j)

    for i in range(m):
        for j in range(n):
            if (i, j) not in visited:
                continue

            for x, y in [
                (i + 2, j),
                (i - 2, j),
                (i + 1, j + 1),
                (i - 1, j - 1),
                (i, j - 2),
                (i, j + 2),
                (i + 1, j - 1),
                (i - 1, j + 1),
            ]:
                if (x, y) not in visited:
                    continue
                shortcut = visited[(i, j)] - visited[(x, y)] - 2
                if shortcut >= saved:
                    res[shortcut] += 1
    return sum(res.values())


if __name__ == "__main__":
    start = time()
    grid = get_input("q20/test")
    print(solve(grid, 1))
    print(time() - start)

    start = time()
    grid = get_input("q20/input")
    print(solve(grid, 100))
    print(time() - start)
