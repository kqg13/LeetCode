# Problem 442: Find duplicates in array

# Given an array of ints, 1 ≤ a[i] ≤ n (n = size of array), some elements
# appear twice and others appear once.

# Find all the elements that appear twice in this array w/o extra space and in O(n) runtime.

# Example: Input: [4, 3, 2, 7, 8, 2, 3, 1], Output: [2, 3]

# Also see Array problems #41 (first missing positive) and
# #448 (find all nums in disappeared array)


class Solution:
    def findDuplicates(self, nums):
        n = len(nums)
        return self.flip(nums, n)

    def flip(self, nums, n):
        results = []
        for i in range(n):
            num = abs(nums[i])
            num -= 1
            if nums[num] > 0:
                nums[num] = -nums[num]
            else:
                results.append(num + 1)
        return results


s = Solution()
nums1 = [4, 3, 2, 7, 8, 2, 3, 1]
nums2 = [5, 4, 6, 7, 9, 3, 10, 9, 5, 6]
print(s.findDuplicates(nums1))
print(s.findDuplicates(nums2))
