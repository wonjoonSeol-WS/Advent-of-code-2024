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
    dp = [0 for _ in range(len(question) + 1)]
    dp[-1] = 1

    for i in range(len(question) - 1, -1, -1):
        for word in dictionary:
            if i + len(word) <= len(question) and question[i : i + len(word)] == word:
                dp[i] += dp[i + len(word)]

    return dp[0]


def word_construction(trie, question):
    dp = [0 for _ in range(len(question) + 1)]
    dp[-1] = 1

    for i in range(len(question) - 1, -1, -1):
        j = i
        curr = trie
        while j < len(question) and question[j] in curr.children:
            curr = curr.children[question[j]]
            j += 1

            if curr.is_word:
                dp[i] += dp[j]
    return dp[0]


def solve(filename):
    trie = Trie()
    # dictionary = []
    res = 0
    with open(filename, "r") as f:
        part1, part2 = f.read().strip().split("\n\n")
        for word in part1.split(", "):
            trie.add_word(word)
            # dictionary.append(word)
        # print(dictionary, len(dictionary))

        for question in part2.split():
            res += word_construction(trie.root, question)  # 0.014930009841918945
            # res += word_construction2(dictionary, question) # 1.4842896461486816

    return res


if __name__ == "__main__":
    start = time()
    # print(solve("q19/test"))
    print(solve("q19/input"))
    print(time() - start)
