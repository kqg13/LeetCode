from itertools import combinations
from collections import defaultdict
import operator as op
from functools import reduce


class Solution:
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = defaultdict(lambda: 0)
        pairs = list(combinations(nums, 2))
        for a, b in pairs:
            product = a * b
            d[product] += 1

        result = 0

        for val in d.values():
            if val > 1:
                result += 8 * self.nChooseR(val, 2)
        return result

    def nChooseR(self, n, r):
        r = min(r, n - r)
        numer = reduce(op.mul, range(n, n - r, -1), 1)
        denom = reduce(op.mul, range(1, r + 1), 1)
        return numer // denom


nums1 = [2, 3, 4, 6]
nums2 = [1, 2, 4, 5, 10]
nums3 = [1, 2, 4, 5, 8, 10, 20, 40]
s = Solution()
print(s.tupleSameProduct(nums3))
# print(s.nChooseR(4, 2))
