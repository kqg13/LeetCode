def findPasswordStrength(password):
    n = len(password)
    result = n
    matrix = [[1] * n for _ in range(n)]
    for i in range(1, n):
        for j in range(n - i):
            left = matrix[i - 1][j]
            right = matrix[i - 1][j + 1]
            if left == right:
                begin_ltr = password[j]
                end_ltr = password[j + i]
                if begin_ltr != end_ltr:
                    matrix[i][j] = left + 1
                else:
                    matrix[i][j] = left
            else:
                matrix[i][j] = min(left, right) + 1
            result += matrix[i][j]
    return result


def findPasswordStrengthDP(password):
    n = len(password)
    result = n
    matrix = [[0]*n for _ in range(n)]
    matrix[0] = [1] * n
    for i in range(1, n):
        for j in range(i, n):
            isIncrement = 0 if password[j] == password[j - i] else 1
            matrix[i][j] = min(matrix[i-1][j], matrix[i-1][j-1]) + isIncrement
            result += matrix[i][j]
    return result

pw = 'good'
print(findPasswordStrength(pw))

