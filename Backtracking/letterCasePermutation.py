# LeetCode Problem 784: Letter Case Manipulation

# Given a string S, we can transform every letter individually to be
# lowercase or uppercase to create another string. Return a list of all
# possible strings we could create. Return the output in any order.

# Examples:
# s1 = "a1b2" ---> ["a1b2", "a1B2", "A1b2", "A1B2"]
# s2 = "3z4" ---> ["3z4", "3Z4"]
# s3 = "12345" ---> ["12345"]
# s4 = "0" ---> ["0"]


# Time: O(N * 2^N) where N = # of alpha letters
class Solution:
    def letterCasePermutation(self, S: str) -> list:
        self.n, self.results = len(S), []
        # self.letterCaseBacktrack(S, [], 0)
        self.letterCaseBacktrackCleaner(S, [], 0)
        return self.results

    def letterCaseBacktrack(self, S, currentPath, currentIndex):
        if len(currentPath) == self.n:
            self.results.append(''.join(currentPath))
            return
        theChar = S[currentIndex]
        if not theChar.isalpha():
            currentPath.append(theChar)
            self.letterCaseBacktrack(S, currentPath, currentIndex + 1)
            currentPath.pop()
        else:
            theCharLower = theChar.lower()
            currentPath.append(theCharLower)
            self.letterCaseBacktrack(S, currentPath, currentIndex + 1)
            currentPath.pop()
            currentPath.append(theChar.upper())
            self.letterCaseBacktrack(S, currentPath, currentIndex + 1)
            currentPath.pop()

    def letterCaseBacktrackCleaner(self, S, currentPath, currentIndex):
        if len(currentPath) == self.n:
            self.results.append(''.join(currentPath))
            return
        theChar = S[currentIndex]
        currentPath.append(theChar)
        self.letterCaseBacktrackCleaner(S, currentPath, currentIndex + 1)
        currentPath.pop()
        if theChar.isalpha():
            currentPath.append(theChar.swapcase())
            self.letterCaseBacktrackCleaner(S, currentPath, currentIndex + 1)
            currentPath.pop()


s = Solution()
s1, s2, s3, s4 = "a1b2", "3z4", "12345", "0"
print(s.letterCasePermutation(s1))
print(s.letterCasePermutation(s2))
print(s.letterCasePermutation(s3))
print(s.letterCasePermutation(s4))
