# 2531: Make Number of Distinct Characters Equal
# https://leetcode.com/problems/make-number-of-distinct-characters-equal/

from collections import Counter


class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        d1, d2 = Counter(word1), Counter(word2)
        n1, n2 = len(d1), len(d2)
        if abs(n2 - n1) > 2:
            return False
        for k1 in d1.keys():
            for k2 in d2.keys():
                d1_c = d1.copy()
                d2_c = d2.copy()

                if k1 not in d2_c:
                    d2_c[k1] = 1
                else:
                    d2_c[k1] += 1

                if k2 not in d1_c:
                    d1_c[k2] = 1
                else:
                    d1_c[k2] += 1

                d1_c[k1] -= 1
                d2_c[k2] -= 1

                if d1_c[k1] == 0:
                    del d1_c[k1]
                if d2_c[k2] == 0:
                    del d2_c[k2]

                if len(d1_c) == len(d2_c):
                    return True
        return False


s = Solution()
word1, word2 = "ac", "b"
word3, word4 = "abcc", "aab"
print(s.isItPossible(word1, word2))
print(s.isItPossible(word3, word4))
