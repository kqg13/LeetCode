# Easy binary search problem 167: Two Sum II - Input array is sorted

# Given an array of integers that is already sorted in ascending order, find
# two numbers such that they add up to a specific target number.
# The function twoSum should return indices of the two numbers such that they
# add up to the target, where index1 must be less than index2.

# Notes:
# Your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution and you may
# not use the same element twice.


class Solution:
    # Time: O(NlogN)
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)):
            low, high = i + 1, len(numbers) - 1
            other = target - numbers[i]
            while low <= high:
                mid = (low + high) // 2
                if numbers[mid] < other:
                    low = mid + 1
                elif numbers[mid] > other:
                    high = mid - 1
                else:
                    return [i + 1, mid + 1]

    # Time: O(N)
    def twoSumTwoPointer(self, numbers, target):
        low, high = 0, len(numbers) - 1
        while low < high:
            s = numbers[low] + numbers[high]
            if s > target:
                high -= 1
            elif s < target:
                low += 1
            else:
                return [low + 1, high + 1]
