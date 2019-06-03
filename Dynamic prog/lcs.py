# Longest Common Subsequence

# Implement a function that returns the longest subsequence common to 2 given
# strings. A subsequence is defined as a group of chars that appear sequentially,
# with no importance given to their actual position in a string. In other words,
# characters do not need to appear consecutively in order to form a subsequence.
# Assume there will only be 1 longest common subsequence.


def longest_common_subsequence(str1, str2):
    r, c = len(str1) + 1, len(str2) + 1
    seq_matrix = [[0 for _ in range(c)] for _ in range(r)]
    path_matrix = [["" for _ in range(c)] for _ in range(r)]

    for i in range(1, r):
        for j in range(1, c):
            top, left = seq_matrix[i - 1][j], seq_matrix[i][j - 1]
            l1, l2 = str1[i - 1], str2[j - 1]
            equal_letter = 1 if l1 == l2 else 0
            diagonal = seq_matrix[i - 1][j - 1] + equal_letter
            if equal_letter:
                seq_matrix[i][j] = diagonal
                path_matrix[i][j] = "diagonal"
            else:
                if top > left:
                    seq_matrix[i][j] = top
                    path_matrix[i][j] = "top"
                else:
                    seq_matrix[i][j] = left
                    path_matrix[i][j] = "left"

    lcs = []
    print_path(str1, path_matrix, lcs, r - 1, c - 1)
    return lcs


def print_path(str1, path_matrix, lcs, i, j):
    if i == 0 or j == 0:
        return
    if path_matrix[i][j] == "diagonal":
        print_path(str1, path_matrix, lcs, i - 1, j - 1)
        lcs.append(str1[i - 1])
    elif path_matrix[i][j] == "top":
        print_path(str1, path_matrix, lcs, i - 1, j)
    elif path_matrix[i][j] == "left":
        print_path(str1, path_matrix, lcs, i, j - 1)


# s1 = "ABCBDAB"
# s2 = "BDCABA"
s1 = "ZXVVYZW"
s2 = "XKYKZPW"
print(longest_common_subsequence(s1, s2))
