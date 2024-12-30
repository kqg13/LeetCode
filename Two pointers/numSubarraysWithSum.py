# 930: Binary Subarrays With Sum
# https://leetcode.com/problems/binary-subarrays-with-sum/description/

from typing import List
from collections import defaultdict


class Solution:
    # prefix sum solution: O(N) one-pass, O(N) space
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d = defaultdict(lambda: 0)
        curr_sum, total_count = 0, 0
        for num in nums:
            curr_sum += num
            if curr_sum == goal:
                total_count += 1

            if curr_sum - goal in d:
                total_count += d[curr_sum - goal]

            d[curr_sum] = d[curr_sum] + 1

        return total_count


s = Solution()

nums1, goal1 = [1, 0, 1, 0, 1], 2  # Expected: 4
nums2, goal2 = [0, 0, 0, 0, 0], 0  # Expected: 15

