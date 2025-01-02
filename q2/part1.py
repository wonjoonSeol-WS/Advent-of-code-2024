filename = "q2/input"
# filename = "q2/test"


def is_safe(report, is_increasing):

    for i in range(1, len(report)):
        # 100 1 2 3
        # 1 100 2 3
        if (
            abs(report[i] - report[i - 1]) > 3
            or (is_increasing and report[i] <= report[i - 1])
            or (not is_increasing and report[i] >= report[i - 1])
        ):
            return False
    return True


res = 0

with open(filename, "r") as f:
    while line := f.readline():
        report = line.split(" ")
        report = list(map(int, report))
        res += is_safe(report, True) or is_safe(report, False)

# time complexity O(n) space complexity O(1)
print(res)
