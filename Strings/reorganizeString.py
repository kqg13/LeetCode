# 767: Reorganize String
# https://leetcode.com/problems/reorganize-string/description/

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
        result = [""] * n

        counter = Counter(s)
        most_common = counter.most_common(1)
        most_common_ele, most_common_freq = most_common[0]

        limit = math.ceil(n/2)
        elements = counter.elements()

        if most_common_freq > limit:
            return ""
        elif most_common_freq == limit:
            for idx in range(0, n, 2):
                result[idx] = most_common_ele
            idx = 1
            for ele in elements:
                if ele == most_common_ele:
                    continue
                result[idx] = ele
                idx += 2
        else:
            idx = 0
            for ele in elements:
                if idx >= n:
                    idx = 1
                result[idx] = ele
                idx += 2

        return "".join(result)


s = Solution()
s1 = "aab"
s2 = "aaab"
s3 = "aabbcc"
s4 = "aabb"

