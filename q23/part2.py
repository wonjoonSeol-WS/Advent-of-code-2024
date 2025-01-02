from collections import defaultdict
from time import time


def get_input(filename):
    adj_list = defaultdict(set)
    with open(filename, "r") as f:
        while line := f.readline().strip():
            # print(line)
            a, b = line.split("-")
            adj_list[a].add(b)
            adj_list[b].add(a)
    return adj_list


def find_groups(adj_list):
    res = set()

    def dfs(curr, visited):
        key = tuple(sorted(visited))
        if key in res:
            return

        res.add(key)
        visited.add(curr)
        for node in adj_list[curr]:
            if node in visited:
                continue

            is_connected = True
            for existing_node in visited:
                if node not in adj_list[existing_node]:
                    is_connected = False
                    break

            if not is_connected:
                continue
            visited.add(node)
            dfs(node, visited)
            visited.remove(node)

    for node in adj_list:
        dfs(node, {node})

    # print(res)
    return max(res, key=len)


if __name__ == "__main__":
    start = time()
    adj_list = get_input("q23/input")
    print(",".join(find_groups(adj_list)))
    print(time() - start)
