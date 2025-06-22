# 1249: Minimum Remove to Make Valid Parentheses
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        split_s = list(s)
        stack = []
        for i, c in enumerate(split_s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if not stack:
                    split_s[i] = ''
                else:
                    stack.pop()
        while stack:
            i = stack.pop()
            split_s[i] = ''

        joined = ''.join(split_s)
        return joined


s = Solution()
s1 = "lee(t(c)o)de)"
s2 = "a)b(c)d"
s3 = "))(("
s.minRemoveToMakeValid(s3)
