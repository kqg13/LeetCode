# AlgoExpert medium string problem: Longest Palindromic Substring

# Write a function that given a string, returns its longest palindromic
# substring. Note that single-character strings are palindromes.

# Input: "abaxyzzyxf"  Output: xyzzyx


# Time: O(), Space: O()
def longestPalindromicSubstring(string):
    if len(string) == 0 or len(string) == 1: return string
    best = 0, 0

    for i, c in enumerate(string):
        # odd length
        start, end = checkPalindrome(i - 1, i + 1, string)
        if end - start > best[1] - best[0]:
            best = start, end
        # even length
        start, end = checkPalindrome(i, i + 1, string)
        if end - start + 1 > best[1] - best[0]:
            best = start, end
    return string[best[0]: best[1] + 1]


def checkPalindrome(i, j, string):
    while i > -1 and j < len(string) and string[i] == string[j]:
        i -= 1
        j += 1
    return i + 1, j - 1


s1 = "abaxyzzyxf"
s2 = "bb"
s3 = "abbaabbca"
s4 = "abbaabba"

print(longestPalindromicSubstring(s1))
print(longestPalindromicSubstring(s2))
print(longestPalindromicSubstring(s3))
print(longestPalindromicSubstring(s4))


