from time import time


def get_next_secret(secret):
    next_secret = ((secret * 64) ^ secret) % 16777216
    next_secret = (next_secret // 32) ^ next_secret
    next_secret = ((next_secret * 2048) ^ next_secret) % 16777216
    return next_secret


def process_input(filename):
    res = 0
    with open(filename) as f:
        while line := f.readline().strip():
            num = int(line)
            secret = num

            for _ in range(2000):
                secret = get_next_secret(secret)
            res += secret
    return res


if __name__ == "__main__":
    start = time()
    print(process_input("q22/input"))
    print(time() - start)
