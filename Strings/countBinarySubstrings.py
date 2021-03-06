import itertools

# Easy string problem 696: Count Binary Substrings

# Give a string s, count the number of non-empty (contiguous) substrings that
# have the same number of 0's and 1's, and all the 0's and all the 1's in these
# substrings are grouped consecutively. Substrings that occur multiple times
# are counted the number of times they occur.

# Input: "00110011" Output: 6
# Explanation: There are 6 substrings that have equal number of consecutive
# 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

# Notice that some of these substrings repeat and are counted the # of times
# they occur.
# Also, "00110011" is not a valid substring because all the 0's (and 1's) are
# not grouped together.


class Solution:
    def countBinarySubstrings(self, s):
        """
        :param s: str
        :return: int
        """
        groups = [len(list(v)) for _, v in itertools.groupby(s)]
        ans = 0
        for i in range(1, len(groups)):
            ans += min(groups[i - 1], groups[i])
        return ans


sol = Solution()
s = "1"
print(sol.countBinarySubstrings(s))
