# String problem 14: Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string.
# All given inputs are in lowercase letters a-z.

# Example 1: Input: ["flower", "flow", "flight"] --> "fl"
# Example 2: Input: ["dog", "racecar", "car"] --> ""
# Example 3: Input: ["leets", "leetcode", "leet", "leeds"] --> "lee"


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        prefix, lex_sorted = "", sorted(strs)
        last = lex_sorted[-1]
        for ltr in lex_sorted[0]:
            if last.startswith(prefix + ltr):
                prefix += ltr
            else:
                break
        return prefix
