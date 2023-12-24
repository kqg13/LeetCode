# 274: H-Index
# https://leetcode.com/problems/h-index/

class Solution:
    # O(N)
    def hIndex(self, citations) -> int:
        n = len(citations)
        c_cumul = [0] * (n + 1)

        for c in citations:
            if c > n:
                c_cumul[n] += 1
            else:
                c_cumul[c] += 1

        accumulator = 0
        for i in range(n, -1, -1):
            accumulator += c_cumul[i]
            if accumulator >= i:
                return i
        return 0

    # O(NlogN)
    def hIndexSorted(self, citations) -> int:
        h = len(citations)
        citations_sorted = sorted(citations)
        for c in citations_sorted:
            if c < h:
                h -= 1
            else:
                return h
        return h


s = Solution()
citations1 = [3, 0, 6, 1, 5]
citations2 = [1, 3, 1]
