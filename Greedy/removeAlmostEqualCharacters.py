# 2957: Remove Adjacent Almost-Equal Characters
# https://leetcode.com/problems/remove-adjacent-almost-equal-characters/

class Solution:
    def removeAlmostEqualCharacters(self, word):
        count, i, n = 0, 0, len(word)
        while i < n - 1:
            first_char, second_char = word[i], word[i + 1]
            if abs(ord(second_char) - ord(first_char)) <= 1:
                count += 1
                i += 2
            else:
                i += 1
        return count


s = Solution()
word1 = "aaaaa"  # Expected: 2
word2 = "abddez"  # Expected: 2
word3 = "zyxyxyz"  # Expected: 3
