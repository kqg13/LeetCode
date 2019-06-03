# Hard Dynamic Programming: 0/1 Knapsack

# You are given an array of arrays. Each subarray in this array holds 2 int
# values and represents an item; the first int is the item's value, and the
# second is the item's weight. You are also given an int representing the max
# capacity of a knapsack that you have. Your goal is to fit items in your
# knapsack, all the while maximizing their combined value. Write a function that
# returns the maximized combined value of the items that you should pick, as well
# as an array of the indices of each item picked. Assume there will only be 1 combo
# of items that maximizes the total value in the knapsack.

# Sample input: [[1, 2], [4, 3], [5, 6], [6, 7]], 10
# Sample output: [10, [1, 3]]


def knap_sack_problem(items, capacity):
    r, c = len(items) + 1, capacity + 1
    matrix = [[0 for _ in range(c)] for _ in range(r)]

    for i in range(1, r):
        for j in range(1, c):
            top = matrix[i - 1][j]
            cur_val, cur_weight = items[i - 1]

            if j - cur_weight < 0:
                left = 0
            else:
                left = matrix[i-1][j - cur_weight] + cur_val

            matrix[i][j] = max(top, left)

    results = [matrix[r - 1][c - 1], []]
    j = c - 1

    for i in range(r - 1, 0, -1):
        if matrix[i][j] == matrix[i - 1][j]:
            continue
        else:
            j = j - items[i - 1][1]
            results[1].append(i - 1)

    results[1] = results[1][::-1]
    return results


def print_matrix(matrix):
    print()
    for r in matrix:
        print(r)


sack = [[1, 2], [4, 3], [5, 6], [6, 7]]
max_capacity = 10
knap_sack_problem(sack, max_capacity)
