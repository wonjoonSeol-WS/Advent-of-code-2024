TARGET = "XMAS"


def get_input(filename):
    grid = []
    with open(filename, "r") as f:
        while line := f.readline().strip():
            row = []
            for char in line:
                row.append(char)
            grid.append(row)
    return grid


def find_words(grid):
    m = len(grid)
    n = len(grid[0])

    def helper(i, j, word_idx, dx, dy):
        while True:
            if i not in range(m) or j not in range(n) or grid[i][j] != TARGET[word_idx]:
                return 0
            if word_idx == len(TARGET) - 1:
                return 1
            i += dx
            j += dy
            word_idx += 1

    ret = 0
    for i in range(m):
        for j in range(n):
            for dx, dy in [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1),
                (1, 1),
                (-1, -1),
                (1, -1),
                (-1, 1),
            ]:
                ret += helper(i, j, 0, dx, dy)
    return ret


if __name__ == "__main__":
    grid = get_input("q4/test")
    print(find_words(grid))

    grid = get_input("q4/input")
    print(find_words(grid))
