# 1493: Longest Subarray of 1's After Deleting One Element
# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        left = result = 0
        first_z = -1
        for right, num in enumerate(nums):
            if num == 0:
                if first_z != -1:
                    result = max(right - left - 1, result)
                    left = first_z + 1
                first_z = right
        result = max(n - left - 1, result)
        return result


s = Solution()
nums1 = [1, 1, 0, 1]  # Expected: 3
nums2 = [0, 1, 1, 1, 0, 1, 1, 0, 1]  # Expected: 5
nums3 = [1, 1, 1]  # Expected: 2
nums4 = [0, 0, 0]  # Expected: 0
