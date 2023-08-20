# 2817: Minimum Absolute Difference Between Elements with Constraint
# https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/

from sortedcontainers import SortedSet


class Solution:
    def minAbsoluteDifference(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        result = float('inf')
        ss = SortedSet()
        for i, num in enumerate(nums[x:]):
            ss.add(nums[i])
            if num <= ss[0]:
                result = min(result, ss[0] - num)
            elif num >= ss[-1]:
                result = min(result, num - ss[-1])
            else:
                index = ss.bisect_left(num)
                diff_left = abs(num - ss[index - 1])
                diff_right = abs(num - ss[index])
                result = min(result, diff_left, diff_right)
        return result


s = Solution()
nums1, x1 = [4, 3, 2, 4], 2
nums2, x2 = [5, 3, 2, 10, 15], 1
nums3, x3 = [1, 2, 3, 4], 3
nums4, x4 = [10, 5, 20, 1, 1, 100, 3, 99, 2], 3
s.minAbsoluteDifference(nums1, x1)
