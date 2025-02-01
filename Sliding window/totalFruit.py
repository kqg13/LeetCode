# 904: Fruits Into Baskets
# https://leetcode.com/problems/fruit-into-baskets/description/

from typing import List
from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        left = result = 0
        freqs = defaultdict(lambda: 0)
        for right in range(n):
            current_fruit = fruits[right]
            freqs[current_fruit] += 1
            while len(freqs) > 2:
                left_fruit = fruits[left]
                freqs[left_fruit] -= 1
                if freqs[left_fruit] == 0:
                    del freqs[left_fruit]
                left += 1
            result = max(result, right - left + 1)
        return result


s = Solution()
fruits1 = [1, 2, 1]  # Expected: 3
fruits2 = [0, 1, 2, 2]  # Expected: 3
fruits3 = [1, 2, 3, 2, 2]  # Expected: 4
fruits4 = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]  # Expected: 5
