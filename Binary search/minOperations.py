# 2702: Minimum Operations to Make Numbers Non-positive
# https://leetcode.com/problems/minimum-operations-to-make-numbers-non-positive/
# https://leetcode.com/problems/minimum-operations-to-make-numbers-non-positive/solutions/3563119/good-binary-search-application-python/

from math import ceil


class Solution:
    def minOperationsAnalytic(self, nums, x: int, y: int) -> int:
        """
        nums: List[int]
        x: int
        y: int
        return: int
        """
        lb_list, ub_list = list(), list()
        for num in nums:
            if num <= y:
                continue
            lb = math.ceil(num / x)
            lb_list.append(lb)
            ub = math.ceil(num / y)
            ub_list.append(ub)
        m = max(lb_list)
        s = 0
        for i in range(len(ub_list)):
            if ub_list[i] > m:
                s += ub_list[i] - lb_list[i]  # Not correct: will not work on nums3
        return m if s <= m else s

    # Time limit exceeded
    def minOperationsGreedy(self, nums, x: int, y: int) -> int:
        """
        nums: List[int]
        x: int
        y: int
        return: int
        """
        opsCount = 0
        while not self.checkAllNonPositive(nums):
            maxIndex = nums.index(max(nums))
            for i in range(len(nums)):
                if i == maxIndex:
                    nums[maxIndex] -= x
                else:
                    nums[i] -= y
            opsCount += 1
        return opsCount

    @staticmethod
    def checkAllNonPositive(nums):
        """
        nums: List[int]
        return: bool
        """
        isAllNonPositive = all(num <= 0 for num in nums)
        return isAllNonPositive

    def minOperations(self, nums, x, y):
        """
        nums: List[int]
        x: int
        y: int
        return: int
        """
        low, high = 0, ceil(max(nums) / y)
        while low < high:
            mid = (low + high) // 2
            canFinish = self.canFinish(nums, x, y, mid)
            if canFinish:
                high = mid
            else:
                low = mid + 1
        return high

    def canFinish(self, nums, x, y, k):
        n_ops = 0
        all_Ys = [num - (y * k) for num in nums]
        delta = x - y
        for num in all_Ys:
            if num > 0:
                n_ops += ceil(num / delta)
                if n_ops > k:
                    return False
        return True


sol = Solution()
nums1, x1, y1 = [3, 4, 1, 7, 6], 4, 2  # Expected: 3
nums2, x2, y2 = [1, 2, 1], 2, 1  # Expected: 1
nums3, x3, y3 = [1, 2, 3, 4, 5], 5, 1  # Expected: 3
