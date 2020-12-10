# String problem 3: Longest Substring w/o Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Given a string, find the length of the longest substring w/o repeating chars.
# Input: "abcabcbb"  Output: 3 ("abc")
# Input: "bbbbb"     Output: 1 ("b")
# Input: "pwwkew"    Output: 3 ("wke") not "pwke" because the latter is subsequence


# Time: O(2N), Space: O(N)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        low, high = 0, 0
        theSet, n = set(), len(s)
        best = 0
        while low < n and high < n:
            if s[high] not in theSet:
                theSet.add(s[high])
                high += 1
                best = max(best, high - low)
            else:
                theSet.remove(s[low])
                low += 1
        return best


# key_index = list(my_dictionary).index(the_key) if the_key in my_dictionary else None
