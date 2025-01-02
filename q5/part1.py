from collections import defaultdict


def is_valid(adj_list, arr):
    visited = set()
    for num in arr:
        for preq in visited:
            if preq in adj_list[num]:
                return False
        visited.add(num)
    return True


def process_input(filename):
    adj_list = defaultdict(set)
    res = 0
    with open(filename, "r") as f:
        string = f.read().strip()
        part1, part2 = string.split("\n\n")

        for line in part1.split("\n"):
            a, b = line.strip().split("|")
            adj_list[a].add(b)

        for line in part2.split("\n"):
            arr = line.strip().split(",")
            if is_valid(adj_list, arr):
                res += int(arr[len(arr) // 2])
    return res


if __name__ == "__main__":
    print(process_input("q5/test"))
    print(process_input("q5/input"))
