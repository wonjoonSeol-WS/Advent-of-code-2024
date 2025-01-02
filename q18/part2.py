from collections import deque
from time import time


def get_input(filename):
    walls = []
    with open(filename, "r") as f:
        while line := f.readline().strip():
            j, i = line.split(",")
            walls.append((int(i), int(j)))
    return walls


def get_grid(m, n):
    return [["." for _ in range(n)] for _ in range(m)]


def add_wall(grid, walls, i):
    x, y = walls[i]
    grid[x][y] = "#"


def init_wall(grid, walls, i):
    for x, y in walls:
        grid[x][y] = "#"


def solve(walls, m, n):
    grid = get_grid(m, n)

    def bfs():
        queue = deque([(0, 0)])
        min_step = 0
        visited = set()
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()

                if (i, j) in visited:
                    continue

                if i == m - 1 and j == n - 1:
                    return min_step

                visited.add((i, j))
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if x in range(m) and y in range(n) and grid[x][y] == "." and (x, y) not in visited:
                        queue.append((x, y))
            min_step += 1
        return -1

    for i in range(len(walls)):
        add_wall(grid, walls, i)
        # only rerun if in paths
        if bfs() == -1:
            return walls[i][::-1]
    return -1


if __name__ == "__main__":
    # walls = get_input("q18/test")
    # print(solve(walls, 7, 7))

    start = time()
    walls = get_input("q18/input")
    print(solve(walls, 71, 71))
    print("time taken", time() - start)
