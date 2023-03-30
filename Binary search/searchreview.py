# Binary search problem 704: Binary Search

# Given a sorted (in ascending order) integer array nums of n elements and a
# target value, write a function to search target in nums. If target exists,
# then return its index, otherwise return -1.

import bisect


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = self.search_helper(nums, target, 0, len(nums) - 1)
        return result

    def search_helper(self, nums, target, low, high):
        mid = (low + high) // 2
        if low <= high:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return self.search_helper(nums, target, mid + 1, high)
            else:
                return self.search_helper(nums, target, low, mid - 1)
        return -1

    def search_iter(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
        return -1

    def search_bisect(self, nums, target):
        i = bisect.bisect_left(nums, target, 0, len(nums) - 1)
        return -1 if nums[i] != target else i

    # LeetCode: #744
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        result = self.nextGreatestLetterHelper(letters, target, 0, len(letters))
        return result

    def nextGreatestLetterHelper(self, letters, target, low, high):
        mid = (low + high) // 2
        if low < high:
            if target >= letters[mid]:
                return self.nextGreatestLetterHelper(letters, target, mid + 1, high)
            else:
                return self.nextGreatestLetterHelper(letters, target, low, mid)
        return letters[low % len(letters) - 1]

    # LeetCode: #852
    def peakIndexInMountainArrayBinary(self, A):
        peak = self.peakIndexInMountainArrayBinaryHelper(A, 0, len(A) - 1)
        return peak

    def peakIndexInMountainArrayBinaryHelper(self, A, low, high):
        mid = (low + high) // 2
        if low < high:
            if A[mid] < A[mid - 1]:
                return self.peakIndexInMountainArrayBinaryHelper(A, low, mid-1)
            elif A[mid] < A[mid + 1]:
                return self.peakIndexInMountainArrayBinaryHelper(A, mid + 1, high)
        return mid

    def subsetsIterative(self, nums):
        self.results = [[]]
        for i in range(len(nums)):
            self.results += [subresult + [nums[i]] for subresult in self.results]
        return self.results


s = Solution()
nums1, target1 = [-1, 0, 3, 5, 9, 12], 9
nums2, target2 = [-1, 0, 3, 5, 9, 12], 2
nums3, target3 = [5], 5
letters1, t1 = ["c", "f", "j"], "j"
print(s.nextGreatestLetter(letters1, t1))
a1 = [0, 2, 1, 0]  # expected: 1
a2 = [24, 69, 100, 99, 79, 78, 67, 36, 26, 19]
a3 = [3, 4, 5, 1]
print(s.peakIndexInMountainArrayBinary(a2))
nums_subsets_1 = [1, 2, 3]
print(s.subsetsIterative(nums_subsets_1))