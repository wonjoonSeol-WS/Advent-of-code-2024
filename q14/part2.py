from PIL import Image
from matplotlib import pyplot as plt


def get_input(filename):
    p = []
    v = []
    with open(filename, "r") as f:
        while line := f.readline().strip():
            p_line, v_line = line.split(" ")
            pos = tuple(map(int, p_line[2:].split(",")))[::-1]
            velocity = tuple(map(int, v_line[2:].split(",")))[::-1]
            p.append(pos)
            v.append(velocity)
    return p, v


def calculate_location(p, v, m, n, t):
    locations = []
    for i in range(len(p)):
        # print(p[i][0], m, p[i][0] % m)
        # print(p[i][1], n, p[i][1] % n)
        x = (p[i][0] + t * v[i][0]) % m
        y = (p[i][1] + t * v[i][1]) % n
        locations.append((x, y))
    return locations


def draw(locations, m, n, i):
    grid = [[(0, 0, 0) for _ in range(n)] for _ in range(m)]
    for x, y in locations:
        grid[x][y] = (255, 255, 255)

    im = Image.new("RGB", (n, m))
    im.putdata([x for row in grid for x in row])
    # resized = im.resize((n * 100, m * 100), resample=0)
    im.save(f"output/{i}.jpg", "JPEG")


def safety_score(locations, m, n):
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    for x, y in locations:
        if x == m // 2 or y == n // 2:
            continue
        if x < m // 2 and y < n // 2:
            q1 += 1
        elif x <= m // 2 and y > n // 2:
            q2 += 1
        elif x > m // 2 and y < n // 2:
            q3 += 1
        else:
            q4 += 1
    return q1 * q2 * q3 * q4


def solve(p, v, m, n):
    idx = []
    scores = []
    for t in range(10000):
        idx.append(t)
        locations = calculate_location(p, v, m, n, t)
        scores.append(safety_score(locations, m, n))
        # if t == 100:
        # print(safety_score(locations, m, n))
        # draw(locations, m, n, t)
    plot(idx, scores)
    return


def plot(idx, scores):
    # print(idx)
    # print(scores)
    plt.plot(idx, scores)
    plt.show()


if __name__ == "__main__":
    # p, v = get_input("q14/test")
    # print(solve(p, v, 7, 11))

    p, v = get_input("q14/input")
    solve(p, v, 103, 101)
