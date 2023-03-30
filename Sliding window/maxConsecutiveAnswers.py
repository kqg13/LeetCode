# 2024: Maximize the Confusion of an Exam
# https://leetcode.com/problems/maximize-the-confusion-of-an-exam/


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        self.answerKey = answerKey
        self.n = len(self.answerKey)
        trueStart = self.findKvalues("T", k)
        s, e = 0, trueStart
        result = 1 if trueStart < self.n else self.n
        while e < self.n:
            e = self.findZeroOrOne("T", e + 1)
            print("e", e)
            result = max(result, e - s)
            s = self.findZeroOrOne("T", s)
            print("s: ", s)
        print("result: ", result)
        return result

    def findZeroOrOne(self, value, index):
        while index < self.n and self.answerKey[index] != value:
            index += 1
        return index

    def findKvalues(self, value, k, start=0):
        for i in range(start, k):
            try:
                position = self.answerKey.index(value, start)
                start = position + 1
            except ValueError:
                return self.n
        return position

    def maxConsecutiveAnswers2(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        left = ret = numT = numF = 0

        for right in range(n):
            if answerKey[right] == 'T':
                numT += 1
            else:
                numF += 1
            while numT > k and numF > k:
                if answerKey[left] == 'T':
                    numT -= 1
                else:
                    numF -= 1
                left += 1
            print("left: ", left, "right: ", right,  "ret: ", ret)
            ret = max(ret, right - left + 1)
        return ret


s = Solution()
answerKey1, k1 = "TTFF", 2  # Expected: 4
answerKey2, k2 = "TFFT", 1  # Expected: 3
answerKey3, k3 = "TFTFFTF", 2
# s.maxConsecutiveAnswers(answerKey1, k1)
# s.maxConsecutiveAnswers(answerKey2, k2)
print(s.maxConsecutiveAnswers2(answerKey3, k3))


