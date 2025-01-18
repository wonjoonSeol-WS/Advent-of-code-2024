def get_input(filename):
    locks = []
    keys = []
    with open(filename, "r") as f:
        lines = f.read().strip()
        parts = lines.split("\n\n")

        for part in parts:
            is_key = False
            rows = part.split("\n")
            col = [0] * len(rows[0])
            size = len(rows)
            for i, line in enumerate(rows):
                for j, char in enumerate(line):
                    if i == 0 and char != "#":
                        is_key = True
                    if char == "#":
                        col[j] += 1

            if is_key:
                keys.append(tuple([val - 1 for val in col]))
            else:
                locks.append(tuple([size - val - 1 for val in col]))
    return locks, keys


def match(locks, keys):
    pairs = 0
    for lock in locks:
        for key in keys:
            is_match = True
            for i in range(len(lock)):
                if lock[i] < key[i]:
                    is_match = False

            if is_match:
                pairs += 1
    return pairs


if __name__ == "__main__":
    # locks, keys = get_input("q25/test")
    locks, keys = get_input("q25/input")
    print(match(locks, keys))

    # print("locks", locks)
    # print("keys", keys)
