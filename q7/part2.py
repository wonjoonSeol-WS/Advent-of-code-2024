filename = "q7/input"
# filename = "q7/test"

from collections import defaultdict
from math import log10, ceil, fmod


def is_possible(arr, target):
    cache = {}

    def recur(i, curr):
        if curr == target and i == len(arr):
            return True
        if curr != target and i >= len(arr):
            return False
        if (i, curr) in cache:
            return cache[(i, curr)]
        
        val = arr[i]
        res = recur(i + 1, curr * val) or recur(i + 1, curr + val)

        if curr > 0:
            res |= recur(i + 1, int(f"{curr}{val}"))
            # res |= recur(i + 1, (10 ** ceil(log10(val))) * curr + val) 
            # res |= recur(i + 1, (10 ** ceil(len(str(val)))) * curr + val) # correct
 
        cache[(i, curr)] = res
        return res
    return recur(0, 0)


def is_possible_dp(arr, target):
    dp = defaultdict(bool)
    dp[0] = True
    for num in arr:
        next_dp = defaultdict(bool)
        for t, val in dp.items():
            # +, *, concat
            next_dp[t + num] |= val
            next_dp[t * num] |= val
            next_dp[int(f"{t}{num}")] |= val
        dp = next_dp 
    return dp[target]


def is_possible_backward(arr, target):
    dp = defaultdict(bool)
    dp[target] = True
    for num in reversed(arr):
        next_dp = defaultdict(bool)
        for t, val in dp.items():
            # +, *, concat
            next_dp[t - num] |= val
            if t % num == 0:
                next_dp[t // num] |= val
            tens = 10 ** len(str(num)) 
            if fmod(t, tens) == num:
                next_dp[t // tens] |= val
        dp = next_dp 
    return dp[0]


res = 0
with open(filename) as f:
    while line := f.readline():
        arr = line.split(" ")
        ans = int(arr[0][:-1])
        arr = arr[1:]
        arr = list(map(int, arr))
        if is_possible_backward(arr, ans):
            res += ans

print(res)  # 105517128211543

