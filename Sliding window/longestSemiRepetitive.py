# 2730: Find the Longest Semi-Repetitive Substring
# https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution:
    def longestSemiRepetitiveSubstring(self, s):
        """
        s: str
        return: int
        """
        left = violations = 0
        result = 1
        n = len(s)
        for right in range(1, n):
            if s[right] == s[right - 1]:
                violations += 1
            while violations == 2:
                left += 1
                if s[left] == s[left - 1]:
                    violations -= 1
            result = max(result, right - left + 1)
        return result


s = Solution()
s1 = "52233"  # Expected: 4
s2 = "5494"  # Expected: 4
s3 = "1111111"  # Expected: 2
