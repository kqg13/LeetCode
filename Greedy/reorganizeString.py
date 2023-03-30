# 767: Reorganize String

# Given a string s, rearrange the characters of s so that any two adjacent chars are not the same.
# Return any possible rearrangement of s or return "" if not possible.

# Examples:
# s1 = "aab" --> "aba"
# s2 = "aaab" --> ""

from collections import Counter
import math


class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        counts = Counter(s)
        freq = counts.most_common()  # returns list of tuples (char, freq)
        most_common_freq = freq[0][1]
        if most_common_freq > math.ceil(n/2):  # not possible
            return ""
        res_list = [""] * n
        order = list(range(0, n, 2)) + list(range(1, n, 2))
        print(order)
        for c, num in freq:
            for _ in range(num):
                idx = order.pop(0)
                res_list[idx] = c
        return "".join(res_list)


s = Solution()
s1 = "aab"
s2 = "aaab"
s3 = "kkekkdde"
s4 = "kkkkeeedd"
print(s.reorganizeString(s4))
