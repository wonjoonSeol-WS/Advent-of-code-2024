from collections import deque
from time import time


numeric_grid = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["#", "0", "A"]]
directional_grid = [["#", "^", "A"], ["<", "v", ">"]]
numeric_start = (3, 2)
directional_start = (0, 2)


def cache_result(grid):
    m = len(grid)
    n = len(grid[0])
    cache = {}
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "#":
                continue

            for x in range(m):
                for y in range(n):
                    if grid[x][y] == "#":
                        continue
                    cache[(grid[i][j], grid[x][y])] = bfs(grid, (i, j), grid[x][y])
    return cache


def bfs(grid, start, char):
    m = len(grid)
    n = len(grid[0])
    q = deque([(*start, [])])
    visited = set([start])
    res = []

    while q:
        for _ in range(len(q)):
            i, j, path = q.popleft()
            visited.add((i, j))

            if grid[i][j] == char:
                path.append("A")
                res.append("".join(path.copy()))
                continue

            # optimisation 1: no zigzag
            for dx, dy, val in [(-1, 0, "^"), (1, 0, "v"), (0, -1, "<"), (0, 1, ">")]:
                x = i + dx
                y = j + dy

                if x not in range(m) or y not in range(n) or grid[x][y] == "#" or (x, y) in visited:
                    continue

                new_path = path.copy()
                new_path.append(val)
                q.append((x, y, new_path))

        if res:
            return res
    return None


def calculate_score(expected, len):
    value = int(expected[:-1])
    print(value, len)
    return value * len


def find_route(grid, expected, cache, start):
    res = [""]
    start = grid[start[0]][start[1]]

    for char in expected:
        new_res = []
        for solution in cache[(start, char)]:
            for route in res:
                new_res.append(route + solution)
        start = char
        res = new_res
        # print("matching", char, res)
    return res


def get_length(key, cache, directional_cache, depth):
    if depth == 0:
        return len(key)

    if (key, depth) in cache:
        return cache[(key, depth)]

    total = 0
    for p1, p2 in zip("A" + key, key):
        min_len = float("inf")
        for solution in directional_cache[(p1, p2)]:
            min_len = min(min_len, get_length(solution, cache, directional_cache, depth - 1))
        total += min_len
    cache[(key, depth)] = total
    return total


def find_shortest(key, cache, directional_cache, depth):
    if depth == 0:
        return len(key)

    if (key, depth) in cache:
        return cache[(key, depth)]

    res = 0
    # print(expected, expected.split("A"))
    for part in key.split("A")[:-1]:  # need to ignore last A in split
        part = part + "A"
        solutions = find_route(directional_grid, part, directional_cache, directional_start)
        total = float("inf")
        for solution in solutions:
            total = min(total, find_shortest(solution, cache, directional_cache, depth - 1))
        res += total
    cache[(key, depth)] = res
    return res


def process_input(filename, depth):
    numeric_cache = cache_result(numeric_grid)
    directional_cache = cache_result(directional_grid)

    cache = {}
    score = 0
    with open(filename, "r") as f:
        while line := f.readline().strip():
            # print("test", line)
            res = find_route(numeric_grid, line, numeric_cache, numeric_start)

            min_total = float("inf")
            for path in res:
                min_total = min(min_total, get_length(path, cache, directional_cache, depth))
            # print("min", min_total)
            score += calculate_score(line, min_total)
    print(score)


if __name__ == "__main__":
    start = time()
    # process_input("q21/test", 2)
    process_input("q21/input", 25)
    print(time() - start)
