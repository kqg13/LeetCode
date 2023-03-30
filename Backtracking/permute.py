# Leetcode #46: Permutations

# Given an array nums of distinct ints, return all possible permutations.
# You can return the answer in any order.

# Examples:
# Input: nums1 = [1, 2, 3] ---> [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
# Input: nums2 = [0, 1] ---> [[0, 1], [1, 0]]
# Input: nums3 = [1] ---> [[1]]


# Time: O(N * N!), Space: O(N * N!) also because there are N! solutions of N elements each
class Solution:
    def permute(self, nums: list):
        self.results = []
        self.permuteBacktrack(nums, [])
        return self.results

    def permuteBacktrack(self, nums, currentPath):
        if not nums:
            self.results.append(currentPath.copy())
        for i in range(len(nums)):
            print("i: ", i)
            new_nums = nums[:i] + nums[i + 1:]
            new_current = currentPath + [nums[i]]
            print("nums: ", nums)
            print("currentPath: ", currentPath)
            self.permuteBacktrack(new_nums, new_current)


s = Solution()
nums1, nums2, nums3 = [1, 2, 3], [0, 1], [1]
print(s.permute(nums1))
# print(s.permute(nums2))
# print(s.permute(nums3))
