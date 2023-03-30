# LeetCode problem 22: 22. Generate Parentheses

# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.

# n1 = 3 --->["((()))","(()())","(())()","()(())","()()()"]
# n2 = 1 ---> ["()"]


class Solution:
    def generateParenthesis(self, n: int):
        self.n = n
        self.results = []
        self.generateParensHelper(0, 0, 0, [])
        print(len(self.results))
        return self.results

    def generateParensHelper(self, depth, openCount, closeCount, currentPath):
        if depth == self.n * 2:
            self.results.append(''.join(currentPath))
            return
        if openCount == closeCount:
            currentPath.append('(')
            self.generateParensHelper(depth + 1, openCount + 1, closeCount, currentPath)
            currentPath.pop()
        elif openCount == self.n:
            currentPath.append(')')
            self.generateParensHelper(depth + 1, openCount, closeCount + 1, currentPath)
            currentPath.pop()
        elif openCount > closeCount:
            currentPath.append('(')
            self.generateParensHelper(depth + 1, openCount + 1, closeCount, currentPath)
            currentPath.pop()
            currentPath.append(')')
            self.generateParensHelper(depth + 1, openCount, closeCount + 1, currentPath)
            currentPath.pop()


s = Solution()
n1, n2, n3 = 3, 1, 4
# print(s.generateParenthesis(n1))
print(s.generateParenthesis(5))

