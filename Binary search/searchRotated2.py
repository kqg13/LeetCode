# Leetcode #81: Search in Rotated Sorted Array II

# There is an int array nums sorted in non-decreasing order (not necessarily w/ distinct vals).

# Before being passed to your function, nums is rotated at an unknown pivot index k s.t. the resulting array is
# [nums[k], nums[k + 1], ..., nums[n - 1], nums[0], nums[1], ..., nums[k - 1]].

# Example: [0, 1, 2, 4, 4, 4, 5, 6, 6, 7] might be rotated at pivot index 5 and becomes [4, 5, 6, 6, 7, 0, 1, 2, 4, 4].
#
# Given the array nums after the rotation and an int target, return T if target is in nums, or F if it is not in nums.

# Sample inputs:
# nums1 = [2, 5, 6, 0, 0, 1, 2], target1 = 0 --> True
# nums2 = [2, 5, 6, 0, 0, 1, 2], target2 = 3 --> False

import math


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums: return False
        if len(nums) == 1: return True if target == nums[0] else False
        if nums[0] < nums[-1]:
            pivot = 0
        else:
            pivot = self.findPivotBefore(nums, 0, len(nums) - 1)

        if pivot == 0:
            low, high = 0, len(nums) -1  # binary search entire array
        elif target >= nums[0]:
            low, high = 0, pivot - 1
        else:
            low, high = pivot, len(nums) - 1

        return self.binarySearch(nums, low, high, target)

    def binarySearch(self, nums, low, high, target):
        mid = (low + high) // 2
        if low <= high:
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                return self.binarySearch(nums, low, mid - 1, target)
            else:
                return self.binarySearch(nums, mid + 1, high, target)
        return False

    def findPivotIndex(self, nums, low, high):
        if nums[0] < nums[-1]:
            return 0
        pivot = (low + high) // 2
        print(low, high, pivot)
        if low <= high:
            if nums[pivot] > nums[pivot + 1]:
                return pivot + 1
            elif nums[pivot] < nums[low]:
                return self.findPivotIndex(nums, low, pivot - 1)
            else:
                return self.findPivotIndex(nums, pivot + 1, high)

    def findPivotBefore(self, nums, low, high):
        if low + 1 == high:
            return high
        mid = math.ceil((low + high) / 2)
        if nums[mid] > nums[low]:
            return self.findPivotBefore(nums, mid, high)
        elif nums[mid] < nums[low]:
            return self.findPivotBefore(nums, low, mid)
        else:
            return self.linearScan(nums, low, high, mid)

    def linearScan(self, nums, low, high, mid):
        min_value, min_index = nums[low + 1], low + 1
        for i in range(low + 1, mid):
            if nums[i] < min_value:
                min_value, min_index = nums[i], low + 1 + i
        if min_value < nums[mid]:
            return min_index
        right_side = nums[mid + 1:high + 1]
        max_right_index = right_side.index(max(right_side)) + mid + 1
        return max_right_index + 1


s = Solution()
nums1, target1 = [2, 5, 6, 0, 0, 1, 2], 0
nums2, target2 = [2, 5, 6, 0, 0, 1, 2], 3
nums3, target3 = [4, 5, 6, 6, 7, 0, 1, 2, 4, 4], 4  # Expected: 5
nums4, target4 = [2, 5, 6, 0, 0, 1, 2], 2  # Expected: 3
nums5, target5 = [4, 5, 6, 7, 0, 1, 2], 100  # Expected: 4
nums6 = [10, 12, 14, 16, 18, 20, 22, 2, 4, 6, 8]  # Expected: 7
nums7, target7 = [0, 2, 4, 6, 8, 0], 8  # Expected: 5
nums8, target8 = [4, 4, 4, 4, 4, 4], 5  # Expected: any
nums9 = [4, 4, 4, 4, 0, 1]  # Expected: 4
nums10 = [1, 2, 3, 4, 5, 6, 7]
nums11, target11 = [1, 0, 1, 1, 1], 0
nums12, target12 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1], 2
nums13, target13 = [2, 2, 2, 0, 2, 2], 0
# print(s.search(nums1, target1))
# print(s.search(nums2, target2))
# print(s.search(nums3, target3))
# print(s.search(nums4, target4))
# print(s.search(nums5, target5))
# print(s.search(nums7, target7))
# print(s.search(nums11, target11))

# print(s.findPivotIndex(nums3, 0, len(nums3) - 1))
# print(s.findPivotIndex(nums4, 0, len(nums4) - 1))
# print(s.findPivotIndex(nums5, 0, len(nums5) - 1))
# print(s.findPivotIndex(nums6, 0, len(nums6) - 1))
# print(s.findPivotIndex(nums7, 0, len(nums7) - 1))
# print(s.findPivotIndex(nums8, 0, len(nums8) - 1))
# print(s.findPivotIndex(nums9, 0, len(nums9) - 1))
# print(s.findPivotIndex(nums11, 0, len(nums11) - 1))

# print(s.findPivotBefore(nums3, 0, len(nums3) - 1))
# print(s.findPivotBefore(nums4, 0, len(nums4) - 1))
# print(s.findPivotBefore(nums5, 0, len(nums5) - 1))
# print(s.findPivotBefore(nums6, 0, len(nums6) - 1))
# print(s.findPivotBefore(nums7, 0, len(nums7) - 1))
# print(s.findPivotBefore(nums8, 0, len(nums8) - 1))
# print(s.findPivotBefore(nums9, 0, len(nums9) - 1))
# print(s.findPivotBefore(nums10, 0, len(nums10) - 1))
# print(s.findPivotBefore(nums11, 0, len(nums11) - 1))
print(s.findPivotBefore(nums13, 0, len(nums13) - 1))