from collections import defaultdict


def check_valid(adj_list, arr):
    visited = set()
    is_valid = True
    for num in arr:
        for preq in visited:
            if preq in adj_list[num]:
                return False
        visited.add(num)
    return is_valid


def correct_ordering(adj_list, arr):
    new_adj_list = defaultdict(set)

    for num in arr:
        for num2 in arr:
            if num == num2:
                continue
            if num2 in adj_list[num]:
                new_adj_list[num].add(num2)
    
    res = []
    visited = set()
    cycle = set()

    def dfs(node):
        if node in cycle:
            return False
        if node in visited:
            return True
        
        cycle.add(node)
        for adj_node in new_adj_list[node]:
            if not dfs(adj_node):
                return False

        res.append(node)
        visited.add(node)
        cycle.remove(node)
        return True

    for node in arr:
        dfs(node)
    # alt kanh's algorithm
    # return res[::-1]
    return res[::-1]

def process_input(filename):
    adj_list = defaultdict(set)
    preq = defaultdict(set)
    res = 0
    with open(filename, "r") as f:
        string = f.read().strip()
        part1, part2 = string.split("\n\n")

        for line in part1.split("\n"):
            a, b = line.strip().split("|")
            adj_list[a].add(b)

        for line in part2.split("\n"):
            arr = line.strip().split(",")
            is_valid = check_valid(adj_list, arr)
            if not is_valid:
                arr = correct_ordering(adj_list, arr)
                print(arr)
                res += int(arr[len(arr) // 2])
    return res

if __name__ == "__main__":
    # print(process_input("q5/test"))
    print(process_input("q5/input"))

