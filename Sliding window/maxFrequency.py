# 1838: Frequency of the Most Frequent Element
# https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/

from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        left = cost = result = 0
        sorted_nums = sorted(nums)
        n = len(sorted_nums)
        if n == 1:
            return 1
        for right in range(1, n):
            gap = sorted_nums[right] - sorted_nums[right - 1]
            mf = right - left
            cost += mf * gap
            while cost > k:
                cost -= sorted_nums[right] - sorted_nums[left]
                left += 1
            result = max(right - left + 1, result)

        return result

    def maxFrequencyAlternate(self, nums: List[int], k: int) -> int:
        left = cost = result = 0
        nums_sorted = sorted(nums)  # do not modify the original array
        n = len(nums_sorted)

        for right in range(n):
            cost += nums_sorted[right]  # Accumulate window sum
            target = nums_sorted[right]

            # violation
            while (target * (right - left + 1)) - cost > k:
                cost -= nums_sorted[left]
                left += 1

            result = max(result, right - left + 1)

        return result


s = Solution()
nums1, k1 = [1, 2, 4], 5  # Expected: 3
nums2, k2 = [1, 4, 8, 13], 5  # Expected: 2
