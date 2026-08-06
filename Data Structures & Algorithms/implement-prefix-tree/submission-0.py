class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if not ch in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.eow = True

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            if not ch in curr.children:
                return False
            curr = curr.children[ch]
        return curr.eow

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if not ch in curr.children:
                return False
            curr = curr.children[ch]
        return True
        