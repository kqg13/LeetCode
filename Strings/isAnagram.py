# String problem 242: Valid Anagram

# Given two strings s and t, write a function to determine if t is an
# anagram of s.

# Follow up: what if the inputs contain unicode chars?
# How would you adapt your solution to such case?

from collections import Counter


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        counter_s = Counter([ltr for ltr in s])
        counter_t = Counter([ltr for ltr in t])
        return counter_s == counter_t
