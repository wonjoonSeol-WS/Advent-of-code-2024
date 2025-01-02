filename = "q9/input"
# filename = "q9/test"

filesystem = []


def defragment(arr):
    n = len(arr)
    l = 0
    r = n - 1
    while True:
        while l < n and arr[l] != ".":
            l += 1
        while r >= 0 and arr[r] == ".":
            r -= 1

        if l > r:
            break

        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

    res = 0
    for i in range(len(arr)):
        if arr[i] == ".":
            break
        res += i * arr[i]
    return res


with open(filename, "r") as f:
    line = f.readline().strip()
    block_id = 0
    for i in range(0, len(line), 2):
        block_size = int(line[i])
        free_space = int(line[i + 1]) if i + 1 < len(line) else 0

        for i in range(block_size):
            filesystem.append(block_id)

        for i in range(free_space):
            filesystem.append(".")
        block_id += 1
    # print(filesystem)
    print(defragment(filesystem))
