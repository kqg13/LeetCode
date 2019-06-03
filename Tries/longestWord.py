# Easy Trie problem 720: Longest Word in Dictionary

# Given a list of strings words representing an English Dictionary, find the
# longest word in words that can be built one character at a time by other
# words in words. If there is more than one possible answer, return the
# longest word with the smallest lexicographical order. If there is no answer,
# return the empty string.

from collections import deque


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
        self.word = ""


# I believe this solution is O(l * w + w) or O(l * w)
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
        current.word = word  # Leaf node stores current word

    def bfs(self):
        q = deque([self.root])
        ans = ""
        while q:
            current = q.popleft()
            for node in current.children.values():
                if node.end_of_word:
                    q.append(node)
                    if len(node.word) > len(ans) or node.word < ans:
                        ans = node.word
        return ans

    def longestWord(self, words) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        return trie.bfs()


# O((l * w) ^ 2) where l is length of the word
class Solution:
    def longestWordBruteForce(self, words) -> str:
        ans = ""
        wordset = set(words)
        for word in words:
            if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                if all(word[:i] in wordset for i in range(1, len(word))):
                    ans = word
        return ans


# Test
s = Solution()
words1 = ["w", "wo", "wor", "worl", "world"]
words2 = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
words3 = ["m", "mo", "moc", "moch", "mocha", "l", "la", "lat", "latt", "latte", "c", "ca", "cat"]
words4 = ["worl", "world"]
print(s.longestWordBruteForce(words3))
t = Trie()
print(t.longestWord(words3))
