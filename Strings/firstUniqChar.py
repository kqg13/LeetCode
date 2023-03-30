# String problem 387:  First Unique Character in a String

# Given an array of strings strs, group the anagrams together. Return the answer in any order.

# Ex 1: Input: s = "leetcode" --> return 0
# Ex 2: Input: s = "loveleetcode" --> return 2


from collections import Counter


# Time: O(N) Space: O(A) where A is size of alphabet
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        theDict = Counter(s)
        for k, v in theDict.items():
            if v == 1:
                return s.find(k)
        return -1
