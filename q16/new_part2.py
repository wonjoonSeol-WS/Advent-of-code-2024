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


def solve(grid):
    start_i, start_j = get_start(grid)
    visited = set()
    locations = set()
    best_cost = float("inf")

    def shortest_path(i, j):
        nonlocal locations, best_cost
        min_heap = [(0, i, j, 0, 1, [])]  # score, i, j, di, dj, path

        while min_heap and min_heap[0][0] <= best_cost:
            score, i, j, dx, dy, path = heapq.heappop(min_heap)
            print(
                score,
                "curr",
                i,
                j,
                "dir",
                dx,
                dy,
                (i, j, dx, dy) in visited,
                (i + dx, j + dy, dx, dy) not in visited,
            )
            visited.add((i, j, dx, dy))

            if grid[i][j] == "E":
                if score <= best_cost:
                    best_cost = score
                    for coord in path:
                        locations.add(coord)
                    locations.add((i, j))
                else:
                    return

            path.append((i, j))

            if grid[i + dx][j + dy] != "#" and (i + dx, j + dy, dx, dy) not in visited:
                heapq.heappush(min_heap, (score + 1, i + dx, j + dy, dx, dy, path))

            for new_dx, new_dy in [(dy, -dx), (-dy, dx)]:
                print(
                    (i, j, new_dx, new_dy) not in visited,
                    grid[i + new_dx][j + new_dy] != "#",
                )
                if (i, j, new_dx, new_dy) not in visited and grid[i + new_dx][j + new_dy] != "#":
                    heapq.heappush(min_heap, (score + 1000, i, j, new_dx, new_dy, path.copy()))
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

    # res = set()
    # for x, y in locations:
    #     res.add((x, y))
    #     res |= cache[(x, y)]
    # plot_grid(grid, res)

    return len(locations)


def plot_grid(grid, locations):
    for x, y in locations:
        grid[x][y] = "O"
    for row in grid:
        print(row)


if __name__ == "__main__":
    grid = get_input("q16/test")
    print(solve(grid))
    # grid = get_input("q16/input")
    # print(solve(grid))
