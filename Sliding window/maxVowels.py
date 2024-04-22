# 1456: Maximum Number of Vowels in a Substring of Given Length
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowel_count, result = 0, 0

        # first time
        for i in range(k):
            if s[i] in vowels:
                vowel_count += 1
        result = vowel_count

        end = len(s)
        for window_end in range(k, end):
            first_ele = s[window_end - k]
            last_ele = s[window_end]

            if first_ele in vowels: vowel_count -= 1
            if last_ele in vowels: vowel_count += 1

            result = max(result, vowel_count)
            if result == k: return result

        return result


s = Solution()
s1, k1 = "abciiidef",  3  # Expected: 3
s2, k2 = "aeiou", 2  # Expected: 2
s3, k3 = "leetcode", 3  # Expected: 2
s4, k4 = "weallloveyou", 7  # Expected: 4
s.maxVowels(s4, k4)
