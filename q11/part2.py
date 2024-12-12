from math import log10


def get_input(filename):
    with open(filename, 'r') as f:
        res = list(map(int, f.read().split(" ")))
    return res

cache = {}
def blink(val, n):
    if (val, n) in cache:
        return cache[(val, n)]
    if n == 0:
        return 1
    if val == 0:
        ret = blink(1, n - 1)
    elif (length := len(str(val))) % 2 == 0:
        left = val // (10 ** (length // 2))
        right = val % (10 ** (length // 2))
        ret = blink(left, n - 1) + blink(right, n - 1)
    else:
        ret = blink(val * 2024, n - 1)

    cache[(val, n)] = ret
    return ret


if __name__ == "__main__":
    data = get_input("q11/test")
    print(sum([blink(val, 1) for val in data]))

    data = get_input("q11/input")
    print(sum([blink(val, 25) for val in data])) 
    print(sum([blink(val, 75) for val in data])) 