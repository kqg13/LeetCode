# 2958: Length of Longest Subarray with at Most K Frequency
# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/description/?envType=company&envId=citadel&favoriteSlug=citadel-six-months

from typing import List
from collections import defaultdict


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(lambda: 0)
        start, curr_max = 0, 0
        result = 0
        for end, num in enumerate(nums):
            freq[num] += 1
            freq_num = freq[num]
            if freq_num > k:
                while freq[num] > k:
                    freq[nums[start]] -= 1
                    start += 1
            curr_max = end - start + 1
            result = max(curr_max, result)

        return result


s = Solution()
nums1, k1 = [1, 2, 3, 1, 2, 3, 1, 2], 2  # Expected: 6
nums2, k2 = [1, 2, 1, 2, 1, 2, 1, 2], 1  # Expected: 2
nums3, k3 = [5, 5, 5, 5, 5, 5, 5], 4  # Expected: 4
nums4, k4 = [1, 2, 3, 4, 1, 2, 1, 2], 1  # Expected: 4
nums5, k5 = [1, 11], 2  # Expected: 2
nums6, k6 = [1, 1, 1, 3], 2  # Expected: 3
nums7, k7 = [1, 1, 1, 2], 2  # Expected: 3
