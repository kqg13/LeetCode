# Medium Array problem 238: Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/

# Given an array nums of n integers where n > 1, return an array output such that output[i] is equal to the
# product of all the elements of nums except nums[i].
# Example: Input:  [1, 2, 3, 4], Output: [24, 12, 8, 6]


# Time: O(n), Space: O(1)
class Solution:
    def productExceptSelf(self, nums):
        """
        :param nums: List[int]
        :return: List[int]
        """
        results = [1] * len(nums)

        # Set running product and loop forward
        prod = 1
        for i in range(len(nums)):
            results[i] = results[i] * prod
            prod = prod * nums[i]
            print(prod, results[i])

        print(results)

        # Reset running product  and loop backwards
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            results[i] = results[i] * prod
            prod = prod * nums[i]
            print(prod, results[i])

        return results


s = Solution().productExceptSelf([2, 3, 1, 5])
print(s)

