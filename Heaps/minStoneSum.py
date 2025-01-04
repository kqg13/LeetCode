# 1962: Remove Stones to Minimize Total
# https://leetcode.com/problems/remove-stones-to-minimize-the-total/description/?envType=company&envId=nvidia&favoriteSlug=nvidia-three-months

from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        return -1

    
s = Solution()
piles1, k1 = [5, 4, 9], 2
piles2, k2 = [4, 3, 6, 7], 3
s.minStoneSum(piles1, k1)
s.minStoneSum(piles2, k2)
