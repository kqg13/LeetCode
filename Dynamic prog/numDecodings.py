# 91: Decode Ways
# https://leetcode.com/problems/decode-ways/description/

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        decodings = self.numDecodingsHelper(0, s, n)
        return decodings

    def numDecodingsHelper(self, index, s, n):
        if index == n:
            return 1

        if int(s[index]) == 0:
            return 0

        if index == n - 1:
            return 1

        result = 0
        result += self.numDecodingsHelper(index + 1, s, n)
        if int(s[index:index + 2]) <= 26:
            result += self.numDecodingsHelper(index + 2, s, n)

        return result

    def numDecodingsDp(self, s: str) -> int:
        if s[0] == '0':
            return 0
        n = len(s)
        dp = [1] * (n + 1)

        for i in range(2, n + 1):
            # Check whether single digit is 0
            if s[i - 1] == '0':
                back_one = 0
            else:
                back_one = dp[i - 1]
            # Check whether double-digit is <= 26
            if s[i - 2] == '1' or (s[i - 2] == '2' and 0 <= int(s[i - 1]) <= 6):
                back_two = dp[i - 2]
            else:
                back_two = 0
            dp[i] = back_one + back_two
        return dp[-1]

