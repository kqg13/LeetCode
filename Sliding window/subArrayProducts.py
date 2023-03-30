# LeetCode 713: Subarray Product Less Than K

# Given an array of positive integers nums, count & print the number of (contiguous)
# subarrays where the product of all elements in the subarray is less than k.

# Example:
# Input: nums1 = [10, 5, 2, 6], k = 100 ---> 8


class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :param nums: List[int]
        :param k: int
        :return: int
        """
        a, b, n = 0, 0, len(nums)
        running_product, count = 1, 0
        while True:
            if a == b == n:
                return count
            # edge case if element > k
            if nums[a] >= k:
                a += 1
                b += 1
                continue
            while b < n and running_product * nums[b] < k:
                running_product *= nums[b]
                b += 1
            count += b - a
            print("a, b, count", a, b, count)
            running_product /= nums[a]
            a += 1


s = Solution()
nums1, k1 = [10, 6, 5, 2], 100
print(s.numSubarrayProductLessThanK(nums1, k1))

