# Medium Array Problem 33: Search in Rotated Sorted Array

# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# i.e., [0, 1, 2, 4, 5, 6, 7] might become [4, 5, 6, 7, 0, 1, 2].

# You are given a target value to search. If found in the array return its
# index, otherwise return -1.  You may assume no duplicate exists in the array.
# Your algorithm's runtime complexity must be in the order of O(log n).

# Example 1: nums = [4, 5, 6, 7, 0, 1, 2], target = 0 ---> 4
# Example 2: nums = [4, 5, 6, 7, 0, 1, 2], target = 3 ---> -1

import math


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if target == nums[0] else -1

        if nums[0] < nums[-1]: # array already sorted
            pivot = 0
        else:
            pivot = self.findPivot(nums, 0, len(nums) - 1)

        if pivot == 0:  # if pivot = 0 do binary search on whole thing
            low, high = 0, len(nums) - 1
        elif target >= nums[0]:
            low, high = 0, pivot - 1
        else:
            low, high = pivot, len(nums) - 1

        return self.binarySearch(nums, low, high, target)

    def binarySearch(self, nums, low, high, target):
        if low > high:
            return -1
        mid = math.floor((low + high) / 2)

        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            return self.binarySearch(nums, mid + 1, high, target)
        else:
            return self.binarySearch(nums, low, mid - 1, target)

    def findPivot(self, nums, low, high):
        if low + 1 == high:
            return high

        mid = math.ceil((low + high) / 2)
        if nums[mid] > nums[low]:
            return self.findPivot(nums, mid, high)
        else:
            return self.findPivot(nums, low, mid)


s = Solution()
nums1, tar1 = [4, 5, 6, 7, 0, 1, 2], 0
print("pivot nums1: ", s.findPivot(nums1, 0, len(nums1) - 1))
print(s.search(nums1, tar1))
nums2, tar2 = [3, 4, 5, 1, 2], 3
print("pivot nums2: ", s.findPivot(nums2, 0, len(nums2) - 1))
print(s.search(nums2, tar2))
nums3, tar3 = [4], 3
# print("pivot nums3: ", s.findPivot(nums3, 0, len(nums3) - 1))
print(s.search(nums3, tar3))
nums4, tar4 = [1, 3], 3
print("pivot nums4: ", s.findPivot(nums4, 0, len(nums4) - 1))
print(s.search(nums4, tar4))
nums5, tar5 = [3, 1], 3
print("pivot nums5: ", s.findPivot(nums5, 0, len(nums5) - 1))
print(s.search(nums5, tar5))
nums6, tar6 = [1, 3, 5], 0
print("pivot nums6: ", s.findPivot(nums6, 0, len(nums6) - 1))
print(s.search(nums6, tar6))
nums7, tar7 = [1, 3, 5, 7, 9], 1
print("pivot nums7: ", s.findPivot(nums7, 0, len(nums7) - 1))
print(s.search(nums7, tar7))
nums8, tar8 = [3, 4, 5, 6, 7, 8, 1, 2], 7
print("pivot nums8: ", s.findPivot(nums8, 0, len(nums8) - 1))
print(s.search(nums8, tar8))


