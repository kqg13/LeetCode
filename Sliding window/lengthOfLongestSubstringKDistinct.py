# 340: Longest Substring with At Most K Distinct Characters
# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        d = dict()
        left = result = 0
        for right, ch in enumerate(s):
            if ch not in d and len(d) <= k:
                d[ch] = 1
            elif ch in d:
                d[ch] += 1

            while len(d) > k:
                leftCh = s[left]
                d[leftCh] -= 1
                if d[leftCh] == 0:
                    del d[leftCh]
                left += 1
            current = right - left + 1
            result = max(result, current)

        return result


s = Solution()
s1, k1 = "eceba", 2  # Expected: 3
s.lengthOfLongestSubstringKDistinct(s1, k1)
s2, k2 = "aa", 1  # Expected: 2
s.lengthOfLongestSubstringKDistinct(s2, k2)
