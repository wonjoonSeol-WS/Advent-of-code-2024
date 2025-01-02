from collections import deque


def get_input(filename):
    walls = []
    with open(filename, "r") as f:
        while line := f.readline().strip():
            j, i = line.split(",")
            walls.append((int(i), int(j)))
    return walls


def get_grid(walls, m, n):
    grid = [["." for _ in range(n)] for _ in range(m)]

    for i, j in walls:
        grid[i][j] = "#"
    return grid


def solve(walls, m, n):
    grid = get_grid(walls, m, n)
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


if __name__ == "__main__":
    walls = get_input("q18/test")
    print(solve(walls[:12], 7, 7))

    walls = get_input("q18/input")
    print(solve(walls[:1024], 71, 71))
