# Write a function that takes in 2 strings and returns the min number of edit
# operations that need to be performed on the first string to obtain the
# second string. There are 3 edit operations: insertion of a char, deletion
# of a char, and substitution of a char for another.

# Sample input: "abc", "yabd"
# Sample output: 2


# Time: O(len(str1) * len(str2)), Space: Same
def edit_distance(str1, str2):
    r, c = len(str1) + 1, len(str2) + 1
    matrix = [[0 for _ in range(c)] for _ in range(r)]

    # Populate rows and cols
    for i in range(r):
        matrix[i][0] = i
    for i in range(c):
        matrix[0][i] = i

    for i in range(1, r):
        for j in range(1, c):
            top, left = matrix[i - 1][j] + 1, matrix[i][j - 1] + 1
            l1, l2 = str1[i - 1], str2[j - 1]
            equal_letter = 0 if l1 == l2 else 1
            diagonal = matrix[i - 1][j - 1] + equal_letter
            matrix[i][j] = min(top, left, diagonal)

    return matrix[r - 1][c - 1]
