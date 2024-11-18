# 66: Plus One
# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits):
        joined_int_plus_1 = int(''.join(map(str, digits))) + 1
        joined_str_plus_1 = str(joined_int_plus_1)
        result = [int(c) for c in joined_str_plus_1]
        return result


s = Solution()
digits1 = [1, 2, 3]
digits2 = [4, 3, 2, 1]
digits3 = [9, 9, 9, 9]
digits4 = [1, 2, 9]
digits5 = [9, 9, 9]
s.plusOne(digits1)
s.plusOne(digits2)
s.plusOne(digits3)
s.plusOne(digits4)
s.plusOne(digits5)