# CTCI string problem 1.4: Palindrome Permutation

# Given a string, write a function to check if it is a permutation of a
# palindrome. The palindrome does not need to be limited to just dictionary
# words.
#
# Example:  Input: Tact Coa, Output: True because permutations include
# "taco cat", "atco cta", etc.


def is_perm_palindrome(phrase):
    stripped = phrase.replace(" ", "")
    counts = [0] * 26
    odd_count = 0

    for ltr in stripped:
        i = ord(ltr) - 96  # ord is unicode rep of a character max = 97
        counts[i] += 1
        if counts[i] % 2 == 0:
            odd_count -= 1
        else:
            odd_count += 1

    return odd_count <= 1
