# Medium sorting problem 215: Kth Largest Element in an Array

# Find the kth largest element in an unsorted array. Note that it is
# the kth largest element in the sorted order, not the kth distinct element.
#
# Example 1: Input: [3, 2, 1, 5, 6, 4] and k = 2, Output: 5
# Example 2: Input: [3, 2, 3, 1, 2, 4, 5, 5, 6] and k = 4 Output: 4

# Notes:
# [1, 4, 5, 7, 0, 6, 2, 8, 9, 3]
# [1, 0, 5, 7, 4, 6, 2, 8, 9, 3]
# [1, 0, 2, 7, 4, 6, 5, 8, 9, 3]
# [1, 0, 2, 3, 4, 6, 5, 8, 9, 7] --> 1 iteration of QS
# [ , , , , , , , 7, 8, 9] --> k = 3 or 7th smallest item


# Time: O(N) Space: O(1)
class Solution:
    def partition(self, arr, low, high):
        divider, pivot = low, high

        for i in range(low, high):
            if arr[i] < arr[pivot]:
                arr[i], arr[divider] = arr[divider], arr[i]
                divider += 1
        arr[pivot], arr[divider] = arr[divider], arr[pivot]
        return divider

    def findKthLargest(self, nums, k):
        """
        :param nums: List[int]
        :param k: int
        :return: int
        """
        low, high = 0, len(nums) - 1
        k = len(nums) - k  # kth largest means n - k smallest
        while 1:
            p = self.partition(nums, low, high)
            if p == k:
                return nums[p]
            elif p < k:
                low = p + 1
            else:
                high = p - 1
