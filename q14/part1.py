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
    # print(p, v)
    return p, v


def calculate_location(p, v, m, n):
    t = 100
    locations = []
    for i in range(len(p)):
        x = (p[i][0] + t * v[i][0]) % m
        y = (p[i][1] + t * v[i][1]) % n
        locations.append((x, y))
    return locations


def solve(p, v, m, n):
    locations = calculate_location(p, v, m, n)
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
    print(q1, q2, q3, q4)
    return q1 * q2 * q3 * q4


if __name__ == "__main__":
    p, v = get_input("q14/test")
    print(solve(p, v, 11, 7))

    p, v = get_input("q14/input")
    print(solve(p, v, 103, 101))
