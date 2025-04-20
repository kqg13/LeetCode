# 1780: Check if Number is a Sum of Power of Three
# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/description/

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        self.n = n
        self.answer = False
        if (self.n**(1/3)).is_integer():
            return True
        self.checkPowersOfThreeHelper(0, 0)
        return self.answer

    def checkPowersOfThreeHelper(self, power, currentSum):
        if currentSum == self.n:
            self.answer = True
            return
        elif self.answer or currentSum > self.n or 3 ** power > self.n:
            return
        else:
            self.checkPowersOfThreeHelper(power + 1, currentSum + 3 ** power)
            self.checkPowersOfThreeHelper(power + 1, currentSum)

    def checkPowersOfThreeBackTrack(self, n, power, currentSum):
        # Base cases
        if currentSum > n:
            return False
        if currentSum == n:
            return True

        current = 3 ** power

        if current > n:
            return False

        take = self.checkPowersOfThreeBackTrack(n, power + 1, currentSum + current)
        if take:
            return True
        no_take = self.checkPowersOfThreeBackTrack(n, power + 1, currentSum)
        return take or no_take


s = Solution()
n1, n2, n3 = 12, 91, 21
print(s.checkPowersOfThree(n1))
print(s.checkPowersOfThree(n2))
print(s.checkPowersOfThree(n3))
