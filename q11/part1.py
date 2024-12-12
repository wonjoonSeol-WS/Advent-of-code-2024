from math import log10


class Node:
    def __init__(self, val=None):
        self.next = None
        self.val = val


def get_input(filename):
    with open(filename, 'r') as f:
        res = list(map(int, f.read().split(" ")))
    return res


def blink(node):
    while node:
        if node.val == 0:
            node.val = 1
        elif (length := len(str(node.val))) % 2 == 0:
            l = node.val // (10 ** (length // 2))
            r = node.val % (10 ** (length // 2))
            next_node = node.next
            node.next = Node(val=r)
            node.next.next = next_node
            node.val = l
            node = node.next
        else:
            node.val *= 2024
        node = node.next


def blinks(data, n):
    dummy = Node()
    curr = dummy
    for num in data:
        curr.next = Node(val=num)
        curr = curr.next

    for i in range(n):
        # print("blink", i)
        blink(dummy.next)

    res = []
    while dummy.next:
        dummy = dummy.next
        res.append(dummy.val)
    print(res)
    return len(res)



if __name__ == "__main__":
    # data = get_input("q11/test")
    # print(blinks(data, 1))

    data = get_input("q11/input")
    for i in range(10):
        print(blinks(data, i))
