# 977: Sorted Squares
# https://leetcode.com/problems/squares-of-a-sorted-array/


class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        low, high = 0, n - 1
        result = list()
        while low != high:
            if abs(nums[high]) >= abs(nums[low]):
                numsToInsert = nums[high] ** 2
                result.insert(0, numsToInsert)
                high -= 1
            else:
                numsToInsert = nums[low] ** 2
                result.insert(0, numsToInsert)
                low += 1
        lastNum = nums[low] ** 2
        result.insert(0, lastNum)
        return result


s = Solution()
nums1 = [-4, -1, 0, 3, 10]
nums2 = [-7, -3, 2, 3, 11]
