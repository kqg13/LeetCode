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
        self.results = 0
        self.vowelsHelper(n, 1)
        return self.results

    def vowelsHelper(self, n, letter):
        if n == 0:
            self.results += 1
            return

        for i in range(1, 6):
            if i >= letter:
                self.vowelsHelper(n - 1, i)


s = Solution()
print(s.countVowelStrings(3))
