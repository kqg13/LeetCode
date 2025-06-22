# 646: Maximum Length of Pair Chain
# https://leetcode.com/problems/maximum-length-of-pair-chain/

from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs_sorted = sorted(pairs, key=lambda p: p[1])
        count = 0
        current = -1001
        for i, (x, y) in enumerate(pairs_sorted):
            if x > current:
                current = y
                count += 1
        return count


s = Solution()
pairs1 = [[1, 2], [2, 3], [3, 4]]  # Expected: 2
pairs2 = [[1, 2], [7, 8], [4, 5]]  # Expected: 3
pairs3 = [[-7, 0], [-5, 1], [-2, 1], [1, 5], [2, 6]]  # Expected: 2
