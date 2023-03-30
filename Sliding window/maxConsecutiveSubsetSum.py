# https://www.youtube.com/watch?v=qqXOZD4zKEg
# Sliding window pattern

# Write a function called maxConsecutiveSubsetSum that accepts a list of ints
# and an int k. Return an int representing max sum of k consecutive elements
# in the array.


def maxConsecutiveSubsetSum(nums, k):
    result = temp_result = sum(nums[:k])

    low, high = 0, k
    while high < len(nums):
        temp_result = temp_result - nums[low] + nums[high]
        result = max(result, temp_result)
        low += 1
        high += 1

    return result


nums1, k1 = [4, 5, 7, 9, 20, 4, 9, 3, 11, 4, 3], 3  # Exp: 36
nums2, k2 = [7, 9, 20, 4, 9, 3, 11, 4, 3], 2  # Exp: 29
