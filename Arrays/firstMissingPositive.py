# Problem 41: First Missing Positive

# Given an unsorted integer array, find the smallest missing positive int.
# elements sequence.
# Your algorithm should run in O(n) complexity and use constant extra space.

# Example 1: [1, 2, 0] --> 3
# Example 2: [3, 4, -1, 1] --> 2
# Example 3: [7, 8, 9, 11, 12] --> 1

# Also see Array problems #448 (find all nums in disappeared array)
# and #442 (find duplicates in array)


# Time: O(N), Space: O(1)
class Solution:
    # Key observation is that missing int must be in the range of 1 ... n + 1
    # In my review I missed that you should decrement the int to conform to index (line 35)
    def firstMissingPositive(self, nums) -> int:
        n = len(nums)
        self.mark(nums, n)
        self.flip(nums, n)
        return self.getIndex(nums, n)

    def mark(self, nums, n):
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

    def flip(self, nums, n):
        for i in range(n):
            num = abs(nums[i])
            if num > n:
                continue
            num -= 1  # important
            if nums[num] > 0:
                nums[num] = -nums[num]

    def getIndex(self, nums, n):
        print(nums)
        for i, num in enumerate(nums):
            if num > 0:
                return i + 1
        # All numbers are present in the set
        return n + 1


n1 = [3, 4, -1, 1]
print(Solution().firstMissingPositive(n1))
