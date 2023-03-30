# LeetCode Problem 1415: The k-th Lexographical String of All Happy Strings of Length n

# A happy string is a string that:
#
# consists only of letters of the set ['a', 'b', 'c'].
# s[i] != s[i + 1] for all vals of i from 1 to s.length - 1 (string is 1-indexed).
# For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and
# strings "aa", "baa" and "ababbc" are not happy strings.
#
# Given two ints n and k, consider a list of all happy strings of length n sorted
# in lexicographical order.
#
# Return the kth string of this list or return an empty string if there are less
# than k happy strings of length n.

# Examples:
# Input1: n = 1, k = 3 --->  "c"
# Explanation: The list ["a", "b", "c"] contains all happy strings of len 1. The 3rd string is "c".
# Input2: n = 1, k = 4 ---> ""
# Explanation: There are only 3 happy strings of length 1.
# Input3: n = 3, k = 9 --> "cab"


class Solution:
    def getHappyString(self, n: int, k: int) -> []:
        self.happy, self.results = "abc", []
        self.getHappyBacktrack(n, k, [], -1)
        sorted_results = sorted(self.results)
        return "" if k > len(sorted_results) else sorted_results[k - 1]

    def getHappyBacktrack(self, n, k, currentList, startLetter):
        if len(currentList) == n:
            self.results.append(''.join(currentList))
            return
        for i in range(0, len(self.happy)):
            if i != startLetter:
                currentList.append(self.happy[i])
                self.getHappyBacktrack(n, k, currentList, i)
                currentList.pop()


s = Solution()
print(s.getHappyString(3, 9))
print(s.getHappyString(1, 4))
print(s.getHappyString(1, 3))
