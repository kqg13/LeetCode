# Problem #90: Subsets II

# Given an int array nums that may contain duplicates, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.


# Input1: nums1 = [1, 2, 2]
# Output1: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]

# Input2: nums2 = [0]
# Output2: [[], [0]]


from collections import Counter


class Solution:
    def subsetsWithDup(self, nums):
        self.counter = Counter(nums)
        self.n, self.results = len(self.counter), []
        self.uniqueNums = list(self.counter.keys())
        self.subsetsWithDupHelper(0, [])
        return self.results

    def subsetsWithDupHelper(self, index, current):
        if index == self.n:
            self.results.append(current.copy())
            return
        uniqueNum = self.uniqueNums[index]
        for i in range(self.counter[uniqueNum] + 1):
            addList = [uniqueNum] * i
            current.extend(addList)
            self.subsetsWithDupHelper(index + 1, current)
            for j in range(i): current.pop()


s = Solution()
nums1, nums2 = [1, 2, 2], [0]
print(s.subsetsWithDup(nums1))
print(s.subsetsWithDup(nums2))
print(s.subsetsWithDup([]))
