# LeetCode problem 169: Majority Element

# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always
# exist in the array.

# Examples:
# nums = [3, 2, 3] ---> 3
# nums2 = [2, 2, 1, 1, 1, 2, 2] ---> 2


class Solution:
    # Time: O(NlogN) Space: O(logN)
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums = nums
        return self.majorityElementHelper(0, len(self.nums) - 1)

    def majorityElementHelper(self, low, high):
        if low == high:
            return self.nums[low]

        mid = (low + high) // 2
        majEleLeft = self.majorityElementHelper(low, mid)
        majEleRight = self.majorityElementHelper(mid + 1, high)

        # Case 1: left & right sides agree on majority element
        if majEleLeft == majEleRight:
            return majEleLeft
        # Case 2: left & right sides disagree on majority element
        leftCount = self.nums.count(majEleLeft)
        rightCount = self.nums.count(majEleRight)
        return majEleLeft if leftCount > rightCount else majEleRight

    # Not used: replaced with count method
    def getDisagreeCount(self, low, high, target):
        count = 0
        for i in range(low, high + 1):
            if self.nums[i] == target: count += 1
        return count
