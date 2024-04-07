# 28: Find the Index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution:
    # O(len_hay * len_need)
    def strStr(self, haystack: str, needle: str) -> int:
        len_need, len_hay = len(needle), len(haystack)
        window_size = len_hay - len_need + 1
        for window_start in range(window_size):
            for i in range(len_need):
                if haystack[window_start + i] != needle[i]:
                    break
                if i == len_need - 1:
                    return window_start
        return -1


s = Solution()
haystack1, needle1 = "sadbutsad", "sad"  # Expected: 0
haystack2, needle2 = "leetcode", "leeto"  # Expected: -1
