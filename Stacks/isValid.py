# Easy problem 20: Valid Parentheses


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        stack = []
        mapping = {")": "(", "]": "[", "}": "{"}

        for paren in s:
            if paren in mapping:
                top = stack.pop() if stack else "#"
                if mapping[paren] != top:
                    return False
            else:
                stack.append(paren)

        return not stack  # Returns whether list is empty


s = Solution()
parens = "()[]{}"
print(s.isValid(parens))
