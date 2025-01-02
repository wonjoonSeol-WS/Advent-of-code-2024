from collections import defaultdict, deque
from time import time


def make_defaultdict():
    return defaultdict(defaultdict)


def get_input(filename):
    known = {}
    questions = defaultdict(make_defaultdict)
    size = 0
    with open(filename) as f:
        lines = f.read().strip()
        part1, part2 = lines.split("\n\n")

        for line in part1.split("\n"):
            name, value = line.split(": ")
            known[name] = int(value)

        for line in part2.split("\n"):
            part1, res = line.split(" -> ")
            a, operator, b = part1.split(" ")

            if b not in questions[a][operator]:
                questions[a][operator][b] = set()
            questions[a][operator][b].add(res)

            if a not in questions[b][operator]:
                questions[b][operator][a] = set()
            questions[b][operator][a].add(res)

            if res[0] == "z":
                size += 1

    return known, questions, size


def solve(known, questions, size):
    res = [0] * size
    q = deque(list(known.keys()))

    while q:
        curr = q.popleft()
        for op, value_dict in questions[curr].items():
            for key, results in value_dict.items():
                if key not in known:
                    continue

                for new_var in results:
                    if new_var in known:
                        continue

                    if op == "AND":
                        known[new_var] = known[curr] and known[key]

                    elif op == "OR":
                        known[new_var] = known[curr] or known[key]

                    elif op == "XOR":
                        known[new_var] = known[curr] ^ known[key]
                    else:
                        raise NotImplementedError

                    if new_var[0] == "z":
                        res[int(new_var[1:])] = known[new_var]

                    # del value_dict[]
                    q.append(new_var)
    # print(list(reversed(res)))
    res = map(str, reversed(res))
    return int("".join(res), base=2)


if __name__ == "__main__":
    start = time()
    known, questions, size = get_input("q24/input")
    print(solve(known, questions, size))
    print(time() - start)
