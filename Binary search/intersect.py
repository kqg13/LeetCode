# Easy binary search problem 349: Intersection of Two Arrays

# Given two arrays, write a function to compute their intersection
# Example 1: Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2], Output: [2]
# Example 2: Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4], Output: [9, 4]
# Note: Each element in the result must be unique and the result can be in any order.


class Solution:
    # Time: O(NlogN)
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1).intersection(set(nums2)))

    # Time: O(NlogN)
    def binary_intersection(self, nums1, nums2):
        if not nums1 and nums2: return nums1
        if not nums2 and nums1: return nums2

        results = set()

        nums1.sort()

        for num in nums2:
            low, high = 0, len(nums1) - 1
            while low <= high:
                mid = (low + high) // 2
                if nums1[mid] < num:
                    low = mid + 1
                elif nums1[mid] > num:
                    high = mid - 1
                else:
                    results.add(num)
                    break

        return list(results)
