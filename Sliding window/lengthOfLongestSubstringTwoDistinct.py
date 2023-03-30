# String problem 159:  Longest Substring with At Most Two Distinct Characters
# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

# Given a string s, find the length of the longest substring t that contains
# at most 2 distinct chars.

# Input: "eceba",   Output: 3, Explanation: "ece"
# Input: "ccaabbb", Output: 5, Explanation: "aabbb"

from collections import defaultdict


# Time: O(2N), Space: O(1)
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        low, high, best = 0, 0, 0
        theDict = defaultdict(lambda: 0)
        n = len(s)
        while low < n and high < n:
            if s[high] not in theDict and len(theDict) == 2:
                theDict[s[low]] -= 1
                if theDict[s[low]] == 0:
                    theDict.pop(s[low])
                low += 1
            else:
                theDict[s[high]] += 1
                high += 1
                best = max(best, sum(theDict.values()))
        return best


s = Solution()
s1, s2, s3 = "eceba", "ccaabbb", "accbbca"
print(s.lengthOfLongestSubstringTwoDistinct(s1))
print(s.lengthOfLongestSubstringTwoDistinct(s2))
print(s.lengthOfLongestSubstringTwoDistinct(s3))
