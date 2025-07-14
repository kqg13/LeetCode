# 769: Max Chunks to Make Sorted
# https://leetcode.com/problems/max-chunks-to-make-sorted/description/?envType=problem-list-v2&envId=monotonic-stack

from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        currentMax = -1
        count = 0
        for i, ele in enumerate(arr):
            currentMax = max(ele, currentMax)
            if ele <= currentMax:
                count += 1
            if currentMax - (count - 1) == 0:
                chunks += 1
        return chunks


s = Solution()
arr1 = [4, 3, 2, 1, 0]  # Expected: 1
arr2 = [1, 0, 2, 3, 4]  # Expected: 4
s.maxChunksToSorted(arr1)
s.maxChunksToSorted(arr2)

