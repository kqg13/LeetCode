# Easy Problem 344: Reverse String


class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]


reverse = Solution()
print(reverse.reverseString("hello"))
print(reverse.reverseString("A man, a plan, a canal: Panama"))
