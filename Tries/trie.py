# Implementation of Trie ADT
# Source: https://www.youtube.com/watch?v=AXjmTQ8LEoI (Tushar Roy)


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            node = current.children.get(char)
            if node is None:
                node = TrieNode()
                current.children[char] = node
            current = node
        current.end_of_word = True

    def search(self, word):
        current = self.root
        for char in word:
            node = current.children.get(char)
            if node is None:
                return False
            current = node
        return current.end_of_word


trie = Trie()
trie.insert('abc')
trie.insert('abgl')
trie.insert('cdf')
trie.insert('abcd')
trie.insert('lmn')
print(trie.search('abgls'))