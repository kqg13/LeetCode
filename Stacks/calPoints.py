# Easy problem 628: Baseball Game


class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for op in ops:
            if self.is_digit(op):
                stack.append(int(op))
            elif op == "C":
                stack.pop()
            elif op == "D":
                stack.append(stack[-1] * 2)
            else:
                stack.append(stack[-1] + stack[-2])
        return sum(stack)

    # I needed this helper method because built-in isdigit() returns False
    # for negative integers
    def is_digit(self, x):
        try:
            int(x)
            return True
        except ValueError:  # if cannot cast to an int, we return False
            return False
