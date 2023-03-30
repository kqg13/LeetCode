# Easy array problem 169: Majority Element

# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always
# exist in the array.


class Solution:
    # Time: O(NlogN) Space: O(1) because we sorted in place
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums) // 2]

    # Divide and Conquer
    # T(n) = 2T(n/2) + 2n = O(nlogn)
    # Each recursive call performs two recursive calls on subslices n/2
    # and two linear scans of size n.
    def majorityElement(self, nums, low=0, high=None):

        def majorityElementRec(low, high):
            if low == high:
                return nums[low]

            mid = (high - low) // 2 + low
            left = majorityElementRec(low, mid)
            right = majorityElementRec(mid + 1, high)

            # if two halves agree on majority element, return it
            if left == right: return left

            # otherwise, count each element and return the "winner"
            left_count = sum(1 for i in range(low, high + 1) if nums[i] == left)
            right_count = sum(1 for i in range(low, high + 1) if nums[i] == right)

            return left if left_count > right_count else right

        return majorityElementRec(0, len(nums) - 1)
