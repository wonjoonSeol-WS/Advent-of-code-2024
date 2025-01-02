filename = "q9/input"
# filename = "q9/test"


class Node:
    def __init__(self, val=None):
        self.next = None
        self.val = val


filesystem = {}
spaces = Node()


def defragment(arr):
    for key in reversed(filesystem.keys()):
        block_id, block_size = filesystem[key]
        prev = spaces
        node = spaces.next
        while node:
            loc_id, free_space = node.val
            if loc_id >= block_id:
                break
            if free_space < block_size:
                prev = prev.next
                node = node.next
                continue
            if free_space == block_size:
                filesystem[key] = (loc_id, block_size)
                prev.next = node.next
                break
            else:
                filesystem[key] = (loc_id, block_size)
                node.val = [loc_id + block_size, free_space - block_size]
                break

        # print(filesystem)
        # temp = []
        # node = spaces
        # while node:
        # temp.append(node.val)
        #     node = node.next
        # print(temp)
    return get_checksum(filesystem)


def get_checksum(filesystem):
    res = 0
    for key, (lock_id, size) in filesystem.items():
        for i in range(size):
            res += key * (lock_id + i)
    return res


with open(filename, "r") as f:
    line = f.readline().strip()
    file_id = 0
    curr = spaces
    for i in range(0, len(line), 2):
        block_size = int(line[i])
        free_space = int(line[i + 1]) if i + 1 < len(line) else 0
        filesystem[i // 2] = (file_id, block_size)

        file_id += block_size
        curr.next = Node(val=[file_id, free_space])
        curr = curr.next
        file_id += free_space

    # print(filesystem)
    # temp = []
    # node = spaces
    # while node:
    #     temp.append(node.val)
    #     node = node.next
    # print(temp)
    print(defragment(filesystem))
