# 2743: Count Substrings w/o Repeating Chars
# https://leetcode.com/problems/count-substrings-without-repeating-character/description/


class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        start, result = 0, 0
        freq_set = set()
        for end, char in enumerate(s):
            if char in freq_set:
                # increment start until no longer in violation
                while s[start] != char:
                    freq_set.remove(s[start])
                    start += 1
                start += 1
            else:
                freq_set.add(char)
            special = end - start + 1
            result += special
        return result


s1 = "abcd"  # Expected: 10
s2 = "ooo"  # Expected: 3
s3 = "abab"  # Expected: 7
