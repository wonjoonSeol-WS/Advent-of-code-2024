from collections import defaultdict

one = []
two = []

filename = "q1/input"
# filename = "q1/test"


def calculate_similarity_score(one, two):
    res = 0
    freq = defaultdict(int)
    for num in two:
        freq[num] += 1

    for num in one:
        res += freq[num] * num

    return res


with open(filename, "r") as f:
    lines = f.readlines()

    for line in lines:
        a, b = line.split("   ")
        one.append(int(a))
        two.append(int(b))


print(calculate_similarity_score(one, two))
