from time import time


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True


def word_construction2(dictionary, question):
    dp = [False for _ in range(len(question) + 1)]
    dp[-1] = True

    for i in range(len(question) - 1, -1, -1):
        for word in dictionary:
            if i + len(word) <= len(question) and question[i : i + len(word)] == word:
                dp[i] |= dp[i + len(word)]
            if dp[i]:
                break
    return dp[0]


def word_construction3(trie, question):
    dp = [False for _ in range(len(question) + 1)]
    dp[-1] = True

    for i in range(len(question) - 1, -1, -1):
        j = i
        curr = trie
        while not dp[i] and j < len(question) and question[j] in curr.children:
            curr = curr.children[question[j]]
            j += 1

            if curr.is_word:
                dp[i] |= dp[j]
    return dp[0]


def word_construction(root, question):
    cache = {}

    def recur(i, curr):
        if (i, curr) in cache:
            return cache[(i, curr)]

        if i >= len(question):
            return curr.is_word

        char = question[i]
        if char not in curr.children:
            cache[(i, curr)] = False
            return False

        res = False
        node = curr.children[char]
        if recur(i + 1, node):
            cache[(i, curr)] = True
            return True

        if node.is_word and recur(i + 1, root):
            res = True

        cache[(i, curr)] = res
        return res

    return recur(0, root)


def solve(filename):
    trie = Trie()
    dictionary = []
    res = 0
    with open(filename, "r") as f:
        part1, part2 = f.read().strip().split("\n\n")
        for word in part1.split(", "):
            trie.add_word(word)
            dictionary.append(word)

        for question in part2.split("\n"):
            # if word_construction(trie.root, question):  # 0.020728111267089844
            # if word_construction2(dictionary, question):    # 0.5456283092498779
            if word_construction3(trie.root, question):  # 0.007400035858154297
                res += 1

    return res


if __name__ == "__main__":
    # print(solve("q19/test"))

    start = time()
    print(solve("q19/input"))
    print(time() - start)
