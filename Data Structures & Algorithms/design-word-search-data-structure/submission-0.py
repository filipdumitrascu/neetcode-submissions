class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class WordDictionary:
    """Trie

    n - len(word), t - num(trie nodes)
    addWord/search: T = O(n)
    S = O(t + n)
    """
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                ch = word[i]

                if ch == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if ch not in curr.children:
                        return False
                    curr = curr.children[ch]

            return curr.end_of_word

        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
