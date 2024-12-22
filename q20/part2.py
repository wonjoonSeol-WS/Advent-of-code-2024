import heapq
from collections import defaultdict, deque
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


def bfs(grid, i, j):
    m = len(grid)
    n = len(grid[0])
    q = deque([(i, j)])
    cost = 0
    visited = set()
    while q and cost < 20:
        for _ in range(len(q)):
            i, j = q.popleft()

            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if x in range(m) and y in range(n) and (x, y) not in visited:
                    visited.add((x, y))
                    q.append((x, y))
        cost += 1
    return visited


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

            # for x, y in bfs(grid, i, j):
            #     if (x, y) not in visited:
            #         continue
            #     shortcut = visited[(i, j)] - visited[(x, y)] - abs(i - x) - abs(j - y)
            #     if shortcut >= saved:
            #         res[shortcut] += 1

            for cheat_len in range(2, 21):
                for dx in range(cheat_len + 1):
                    dy = cheat_len - dx
                    for x, y in set(
                        [  # must check for duplicates
                            (i + dx, j + dy),
                            (i - dx, j - dy),
                            (i - dx, j + dy),
                            (i + dx, j - dy),
                        ]
                    ):
                        if (x, y) not in visited:
                            continue
                        shortcut = visited[(x, y)] - visited[(i, j)] - cheat_len
                        if shortcut >= saved:
                            res[shortcut] += 1

    # print(dict(sorted(res.items(), key=lambda x: x[0])))
    return sum(res.values())


if __name__ == "__main__":
    start = time()
    grid = get_input("q20/test")
    print(solve(grid, 50))
    print(time() - start)

    start = time()
    grid = get_input("q20/input")
    print(solve(grid, 100))
    print(time() - start)
