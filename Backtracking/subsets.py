# Problem #78: Subsets

# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets.

# Input1: nums1 = [1, 2, 3]
# Output1: [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]

# Input2: nums2 = [0]
# Output2: [[], [0]]


# Time: O(N * 2 ^N) - N because of copying; Space: O(N)
class Solution:
    def subsets(self, nums: list):
        self.results = []
        # self.subsetsIterative(nums)
        # self.subsetsBacktrack(nums, [], 0)
        self.subsetsBacktrackBetter(nums, [], 0)
        return self.results

    def subsetsIterative(self, nums: list):
        for i in range(len(nums)):
            self.results += [subresult + [nums[i]] for subresult in self.results]

    def subsetsBacktrack(self, nums: list, current, index):
        self.results.append(current.copy())
        for i in range(index, len(nums)):
            current.append(nums[i])
            self.subsetsBacktrack(nums, current, i + 1)
            current.pop()

    def subsetsBacktrackBetter(self, nums, currentSet, index):
        if index == len(nums):
            self.results.append(currentSet.copy())
            return
        # 'Including' recursive call
        currentSet.append(nums[index])
        self.subsetsBacktrackBetter(nums, currentSet, index + 1)
        currentSet.pop()
        # 'Excluding' recursive call
        self.subsetsBacktrackBetter(nums, currentSet, index + 1)


s = Solution()
nums1 = [1, 2, 3]
nums2 = [0]
# print(s.subsets(nums1))
print(s.subsets(nums1))
