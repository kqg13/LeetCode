# LeetCode Problem 1641: Count Sorted Vowel Strings

# Given an int n, return the # of strings of length n that consist only of
# vowels (a, e, i, o, u) and are lexicographically sorted.
#
# A string s is lexicographically sorted if for all valid i, s[i] is the same as
# or comes before s[i + 1] in the alphabet.

# Examples:
# Input1: n = 1 ---> 5
# Explanation: The 5 sorted strings that consist of vowels only are ["a", "e", "i", "o", "u"]
# Input2: n = 2 ---> 15
# Input3: n = 33 ---> 66045


class Solution:
    def countVowelStrings(self, n: int) -> int:
        self.result = 0
        self.vowelHelper(n, 1)
        return self.result

    def vowelHelper(self, n, lastChar):
        if n == 0:
            return 1
        self.result = 0
        for i in range(lastChar, 6):
            self.result += self.vowelHelper(n - 1, i)
        return self.result


s = Solution()
print(s.countVowelStrings(3))
