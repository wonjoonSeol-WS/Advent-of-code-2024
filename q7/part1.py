filename = "q7/input"
# filename = "q7/test"

from collections import defaultdict


def is_possible(arr, target):
    # O(n * t) O(t)
    dp = defaultdict(bool)
    dp[0] = True
    for num in arr:
        next_dp = defaultdict(int)
        for t, val in dp.items():
            next_dp[t + num] |= val
            next_dp[t * num] |= val
        dp = next_dp
    return dp[target]

    # top-down time O(n * t) space O(n * t)
    # cache = {}

    # def recur(i, curr):
    #     if curr == target and i == len(arr):
    #         return True
    #     if curr != target and i >= len(arr):
    #         return False
    #     if (i, curr) in cache:
    #         return cache[(i, curr)]

    #     val = arr[i]
    #     res = recur(i + 1, curr * val) or recur(i + 1, curr + val)
    #     cache[(i, curr)] = res
    #     return res
    # return recur(0, 0)


res = 0
with open(filename) as f:
    while line := f.readline():
        arr = line.split(" ")
        ans = int(arr[0][:-1])
        arr = arr[1:]
        arr = list(map(int, arr))
        if is_possible(arr, ans):
            res += ans

print(res)  # 3245122495150
