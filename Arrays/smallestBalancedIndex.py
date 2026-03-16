# 3862: Find the Smallest Balanced Index
# https://leetcode.com/problems/find-the-smallest-balanced-index/

class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return -1
        sums_runner = sum(nums)
        prods_runner = 1
        for i in range(n - 1, 0, -1):
            sums_runner -= nums[i]
            # print("i: ", i, "sums_runner: ", sums_runner, "prods_runner: ", prods_runner, type(prods_runner))
            if sums_runner == prods_runner:
                return i
            if sums_runner < prods_runner:
                return -1
            prods_runner *= nums[i]
        return -1


s = Solution()
nums1 = [2, 1, 2]  # Expected: 1
nums2 = [2, 8, 2, 2, 5]  # Expected: 2
nums3 = [1]  # Expected: -1
nums4 = [999, 818, 984, 995, 841, 822, 984, 978, 960, 997, 896, 926, 759, 961, 1000, 562, 1, 1, 1, 87, 4, 1, 40]  # Expected: 15
