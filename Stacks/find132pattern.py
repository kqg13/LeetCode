# LeetCode Problem 456: 132 Pattern

# Given an array of n ints nums, a 132 pattern is a subsequence of three ints
# nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].
#
# Return true if there is a 132 pattern in nums, otherwise, return false.
# Could you come up with the O(NlogN) or O(N) solution?

# Example 1: nums1 = [1, 2, 3, 4] --> False
# Example 2: nums2 = [3, 1, 4, 2] --> True because [1, 4, 2] is 132 pattern
# Example 2: nums3 = [6, 12, 3, 4, 6, 11, 20] --> True because [6, 12, 11] is 132 pattern

from collections import deque


class Solution:
    def find132pattern(self, nums) -> bool:
        stack = deque()
        mins = self.createMins(nums)
        if len(nums) < 3:
            return False
        stack.append(nums[-1])  # Push last element
        for j in range(len(nums) - 2, -1, -1):
            if nums[j] > mins[j]:
                while len(stack) > 0 and self.peek(stack) <= mins[j]:
                    stack.pop()
                if len(stack) > 0 and self.peek(stack) < nums[j]:
                    return True
                stack.append(nums[j])
        return False

    def createMins(self, nums):
        mins = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            mins[i] = min(mins[i - 1], nums[i])
        return mins

    def peek(self, stack):
        if len(stack) > 0:
            return stack[-1]


s = Solution()
nums1 = [1, 2, 3, 4]
nums2 = [3, 1, 4, 2]
nums3 = [6, 12, 3, 4, 6, 11, 20]
print(s.find132pattern(nums1))
