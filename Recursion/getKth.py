# 1387: Sort Integers by Power Value
# https://leetcode.com/problems/sort-integers-by-the-power-value/


class Solution(object):
    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        results = list()
        self.memo = {1: 0}
        for i in range(lo, hi + 1):
            power = self.powerHelper(i)
            results.append((power, i))
        sorted_power = sorted(results)
        return sorted_power[k - 1][1]

    def powerHelper(self, i):
        count = 0
        while i != 1:
            if i in self.memo:
                return self.memo[i] + count
            if i % 2 == 0:
                i /= 2
            else:
                i = 3 * i + 1
            count += 1
        self.memo[i] = count
        return count
