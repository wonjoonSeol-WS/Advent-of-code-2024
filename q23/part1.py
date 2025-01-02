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


def find_groups(adj_list, depth=3):
    res = set()
    for start_node in adj_list.keys():
        for adj_node in adj_list[start_node]:
            for final_node in adj_list[adj_node]:
                if start_node in adj_list[final_node]:
                    res.add(tuple(sorted([start_node, adj_node, final_node])))

    res = [val for val in res if any(x[0] == "t" for x in val)]  # can use startwith
    return res


if __name__ == "__main__":
    start = time()
    adj_list = get_input("q23/input")
    components = find_groups(adj_list)
    print(len(components))
    print(time() - start)
