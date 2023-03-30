# 26: Remove Duplicates from Sorted Array
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.k = 0
        left = self.findLeft(nums)
        if left == -1:
            return self.k + 1
        curr = nums[left]
        right = self.findRight(nums, left)
        if right == -1:
            return self.k
        self.doSwaps(nums, curr, left, right)
        return self.k

    def doSwaps(self, nums, curr, left, right):
        while True:
            nums[left], nums[right] = nums[right], nums[left]
            curr = nums[left]
            left += 1
            self.k += 1
            while right < len(nums) and nums[right] <= curr:
                right += 1
            if right == len(nums): break

    def findLeft(self, nums):
        for i in range(len(nums) - 1):
            self.k += 1
            if nums[i] == nums[i + 1]:
                l = i + 1
                return l
        return -1

    def findRight(self, nums, left):
        for i in range(left + 1, len(nums)):
            if nums[i] > nums[left]:
                r = i
                return r
        return -1


s = Solution()
nums1 = [1, 1, 2]
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
nums3 = [1, 1, 1]
nums4 = [1, 2, 3, 4, 5]
# s.removeDuplicates(nums1)
s.removeDuplicates(nums2)
# s.removeDuplicates(nums3)
# s.removeDuplicates(nums4)
