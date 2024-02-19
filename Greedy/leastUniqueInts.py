# 1481: Least Number of Unique Integers after K Removals
# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/

from collections import Counter


class Solution:
    def findLeastNumOfUniqueIntsNlogN(self, arr, k):
        cntr = Counter(arr)

        sorted_freqs = sorted(cntr.values(), key=lambda v: v, reverse=False)

        result = len(cntr.keys())

        for frequency in sorted_freqs:
            if k >= frequency:
                k -= frequency
                result -= 1

        return result

    # O(N)
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        arr: List[int]
        k: int
        return: int
        """
        cntr = Counter(arr)
        result = len(cntr.keys())

        # populate budget list
        budget = [0] * k
        for _, v in cntr.items():
            if v <= k:
                budget[v - 1] += 1

        revised_k = k
        for i in range(1, k + 1):
            if i > revised_k:
                break
            if budget[i - 1] == 0:
                continue

            quotient = revised_k // i
            allocation = min(quotient, budget[i - 1])
            revised_k -= allocation * i

            result -= allocation

        return result


s = Solution()
arr1, k1 = [5, 5, 4], 1  # Expected: 1
arr2, k2 = [4, 3, 1, 1, 3, 3, 2], 3  # Expected: 2
