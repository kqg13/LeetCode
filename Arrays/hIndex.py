# 274: H-Index
# https://leetcode.com/problems/h-index/

class Solution:
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
