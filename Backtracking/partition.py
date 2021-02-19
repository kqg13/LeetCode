# Backtrack problem #131: Palindrome Partitioning

# Given a string s, partition s such that every substring of the partition is
# a palindrome. Return all possible palindrome partitioning of s.

# Examples:
# string1 = "aab" --->  [["a", "a", "b"], ["aa", "b"]]
# string2 = ""a" ---> [["a"]]


class Solution:
    def partition(self, s: str):
        self.results = []
        self.partitionHelper(s, [])
        return self.results

    def partitionHelper(self, substring, currentList):
        if not substring:
            self.results.append(list(currentList))

        n = len(substring) + 1

        for i in range(1, n):
            left, right = substring[0:i], substring[i:n]
            if self.isPalindrome(left):
                currentList.append(left)
                self.partitionHelper(right, currentList)
                currentList.pop()

    def isPalindrome(self, s):
        return s == s[::-1]


s = Solution()
string1, string2 = "aab", "a"
print(s.partition(string1))
# s.partition(string2)
# print(s.isPalindrome("amanaplanacanalpanama"))

