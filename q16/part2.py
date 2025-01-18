from collections import defaultdict
import sys
import heapq

sys.setrecursionlimit(1000000)


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


class AutoIncrement:
    def __init__(self):
        self.counter = 0

    def get_next(self):
        self.counter += 1
        return self.counter


autoincrement = AutoIncrement()


def solve(grid):
    m = len(grid)
    n = len(grid[0])

    start_i, start_j = get_start(grid)
    goal_i, goal_j = get_end(grid)
    visited = set()
    locations = set()

    min_scores = [[float("inf") for _ in range(n)] for _ in range(m)]
    cache = defaultdict(set)

    def shortest_path(i, j):
        nonlocal locations
        min_heap = [(0, i, j, 0, 1, 0)]  # score, i, j, di, dj, idx

        while min_heap and min_heap[0][0] <= min_scores[goal_i][goal_j]:

            score, i, j, dx, dy, idx = heapq.heappop(min_heap)
            if i in range(m) and j in range(n) and grid[i][j] == "E":
                locations |= cache[idx].copy()
                locations.add((i, j))
                return

            cache[idx].add((i, j))
            if score <= min_scores[i][j]:
                min_scores[i][j] = score
                cache[(i, j)] |= cache[(idx)]

            if i + dx in range(m) and j + dy in range(n) and grid[i + dx][j + dy] != "#":
                heapq.heappush(min_heap, (score + 1, i + dx, j + dy, dx, dy, idx))

            # print(score, "curr", i, j, "dir", dx, dy)
            if (i, j) not in visited:
                for new_dx, new_dy in get_next_direction(dx, dy):
                    new_idx = autoincrement.get_next()
                    cache[new_idx] = cache[idx].copy()
                    heapq.heappush(min_heap, (score + 1000, i, j, new_dx, new_dy, new_idx))
            visited.add((i, j))
        return -1

    # def dfs(i, j, dx, dy, score, curr):
    #     nonlocal locations, best_score
    #     if i not in range(m) or j not in range(n) or grid[i][j] == "#" or (i, j, dx, dy) in visited or best_score < score:
    #         return

    #     # print(i, j, dx, dy, score)
    #     if grid[i][j] == "E":
    #         locations.add((i, j, 0, 0))
    #         if score == best_score:
    #             locations |= visited.copy()
    #         elif score < best_score:
    #             best_score = score
    #             locations = set()
    #             locations = visited.copy()
    #         return

    #     visited.add((i, j, dx, dy))

    #     dfs(i + dx, j + dy, dx, dy, 1 + score, curr)
    #     for new_dx, new_dy in get_next_direction(dx, dy):
    #         if i + new_dx in range(m) and j + new_dy in range(n) and grid[i + new_dx][j + new_dy] != "#":
    #             dfs(i, j, new_dx, new_dy, 1000 + score, curr)
    #     visited.remove((i, j, dx, dy))

    shortest_path(start_i, start_j)
    # print(locations)

    res = set()
    for x, y in locations:
        res.add((x, y))
        res |= cache[(x, y)]
    # plot_grid(grid, res)

    return len(res)


def plot_grid(grid, locations):
    for x, y in locations:
        grid[x][y] = "O"
    for row in grid:
        print(row)


if __name__ == "__main__":
    grid = get_input("q16/test")
    # print(solve(grid))
    # grid = get_input("q16/input")
    print(solve(grid))
