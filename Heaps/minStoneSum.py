# 1962: Remove Stones to Minimize Total
# https://leetcode.com/problems/remove-stones-to-minimize-the-total/description/?envType=company&envId=nvidia&favoriteSlug=nvidia-three-months
# why is heapify O(N)? See visual: https://stackoverflow.com/questions/9755721/how-can-building-a-heap-be-on-time-complexity


from typing import List
import heapq
import math


class Solution:
    # O(N + k*log(N))
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles_copy = [-1 * num for num in piles]
        heapq.heapify(piles_copy)  # O(N)
        for _ in range(k):  # O(k * log(N) )
            max_element = heapq.heappop(piles_copy)
            operation = max_element - math.ceil(max_element / 2)
            heapq.heappush(piles_copy, operation)
        result = sum(piles_copy) * -1
        return result


s = Solution()
piles1, k1 = [5, 4, 9], 2  # Expected: 12
piles2, k2 = [4, 3, 6, 7], 3  # Expected: 12
