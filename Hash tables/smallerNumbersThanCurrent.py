# 1365: How Many Numbers Are Smaller Than the Current Number
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/


class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        d = self.createDict(n, nums)
        results = self.mapResults(n, nums, d)
        return results

    def mapResults(self, n, nums, d):
        results = [0] * n
        for i, num in enumerate(nums):
            results[i] = d[nums[i]]
        return results

    def createDict(self, n, nums):
        sorted_nums = sorted(nums)
        d = dict()
        for i in range(n):
            if sorted_nums[i] not in d:
                d[sorted_nums[i]] = i
        return d


s = Solution()
nums1 = [8, 1, 2, 2, 3]  # [4,0,1,1,3]
s.smallerNumbersThanCurrent(nums1)
