# 386: Lexical Order
# https://leetcode.com/problems/lexicographical-numbers/description/?envType=problem-list-v2&envId=depth-first-search

from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        self.results = []
        self.limit = n
        for i in range(1, 10):
            self.dfs(i)
        return self.results

    def dfs(self, current):
        if current > self.limit:
            return
        self.results.append(current)
        for i in range(10):
            next_num = (current * 10) + i
            self.dfs(next_num)


s = Solution()
n1 = 13  # Expected: [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
n2 = 2  # Expected: [1, 2]
