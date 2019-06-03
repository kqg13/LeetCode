# Medium Trie problem 677: Map Sum Pairs
# https://leetcode.com/problems/map-sum-pairs/


class TrieNode:
    def __init__(self, val=0):
        self.children = {}
        self.val = val


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        diff = val - self.map.get(key, 0)
        self.map[key] = val
        current = self.root
        for letter in key:
            if letter not in current.children:
                current.children[letter] = TrieNode(val)
            else:
                current.children[letter].val += diff
            current = current.children[letter]

    def sum(self, prefix: str) -> int:
        current = self.root
        for letter in prefix:
            if letter not in current.children:
                return 0
            current = current.children[letter]
        return current.val


obj = MapSum()
obj.insert("apple", 3)
obj.insert("app", 2)
obj.insert("api", 10)
obj.insert("apin", 4)
print(obj.sum("api"))

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key, val)
