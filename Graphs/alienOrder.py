# LeetCode #269: Alien Dictionary

# There is a new alien language that uses English alphabet. But, the order among the letters is unknown to you.
#
# You are given a list of strings words from the alien language's dictionary, where
# the strings in words are sorted lexicographically by the rules of this new language.
#
# Return a string of the unique letters in the new alien language sorted in lexicographically
# increasing order by the new language's rules. If there is no solution, return "".
# If there are multiple solutions, return any of them.
#
# A string s is lexicographically smaller than a string t if at the first letter where they
# differ, the letter in s comes before the letter in t in the alien language. If the
# first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.
#
# Examples:
# words1 = ["wrt", "wrf", "er", "ett", "rftt"] ---> "wertf"
# words2 = ["z", "x"] ---> "zx"
# words3 = ["z", "x", "z"] ---> ""


from collections import deque
from collections import defaultdict


class Solution:
    def alienOrder(self, words):
        """
        :param words: List[str]
        :return: str
        """
        self.nodes = {c for word in words for c in word}
        self.indegrees = defaultdict(int)
        check = self.buildGraph(words)
        return self.topologicalSort() if check else ""

    def buildGraph(self, words):
        self.graph = defaultdict(list, {node: list() for node in self.nodes})
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            if len(word1) > len(word2) and word2 == word1[:len(word2)]:
                return False
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    self.graph[c1].append(c2)
                    self.indegrees[c2] += 1
                    break
        return True

    def topologicalSort(self):
        zero_indegrees_q = deque(node for node in self.nodes if node not in self.indegrees)
        results = ""
        while zero_indegrees_q:
            letter = zero_indegrees_q.popleft()
            results += letter

            for nextLetter in self.graph[letter]:
                self.indegrees[nextLetter] -= 1
                if self.indegrees[nextLetter] == 0:
                    zero_indegrees_q.append(nextLetter)
        return results if len(results) == len(self.nodes) else ""


words1 = ["wrt", "wrf", "er", "ett", "rftt"]
words2 = ["z", "x"]
words3 = ["z", "x", "z"]
words4 = ["abc", "ab"]
s = Solution()
print(s.alienOrder(words1))
print(s.alienOrder(words2))
print(s.alienOrder(words3))
print(s.alienOrder(words4))
