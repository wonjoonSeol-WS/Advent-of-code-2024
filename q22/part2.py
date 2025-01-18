from time import time
from collections import defaultdict


def get_next_secret(secret):
    next_secret = ((secret * 64) ^ secret) % 16777216
    next_secret = (next_secret // 32) ^ next_secret
    next_secret = ((next_secret * 2048) ^ next_secret) % 16777216
    return next_secret


def process_input(filename):
    prices = []
    diff_list = []
    seq_totals = defaultdict(int)
    with open(filename) as f:
        while line := f.readline().strip():
            num = int(line)
            secret = num
            prev = secret % 10
            arr = []
            diff = []
            for _ in range(2000):
                secret = get_next_secret(secret)
                price = secret % 10
                arr.append(price)
                diff.append(price - prev)
                prev = price

            prices.append(arr)
            diff_list.append(diff)
    return prices, diff_list


def get_maximum_banana(prices, diff_list):
    banana = defaultdict(int)
    for i in range(len(prices)):
        visited = set()
        for j in range(len(prices[0]) - 4):
            seq = tuple(diff_list[i][j : j + 4])

            if seq in visited:
                continue
            banana[seq] += prices[i][j + 3]
            visited.add(seq)
    return max(banana.values())


if __name__ == "__main__":
    start = time()
    # prices, diff_list = process_input("q22/test4")
    prices, diff_list = process_input("q22/input")
    print(get_maximum_banana(prices, diff_list))
    print(time() - start)
