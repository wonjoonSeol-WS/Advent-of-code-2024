filename = "q2/input"
# filename = "q2/test"


def is_safe(report, is_increasing, chance=1):
    prev = report[0]
    for i in range(1, len(report)):
        if (
            abs(report[i] - prev) > 3
            or (is_increasing and report[i] <= prev)
            or (not is_increasing and report[i] >= prev)
        ):
            if chance > 0:
                chance -= 1
                continue
            else:
                return False
        prev = report[i]
    return True


res = 0

with open(filename, "r") as f:
    while line := f.readline().strip():
        report = line.split(" ")
        report = list(map(int, report))
        res += (
            is_safe(report, True, 1)
            or is_safe(report, False, 1)
            or is_safe(report[1:], True, 0)
            or is_safe(report[1:], False, 0)
        )

# time complexity O(n) space complexity O(1)
print(res)
