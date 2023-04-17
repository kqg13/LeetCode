def knapsack_0_1(profits, weights, capacity):
    n = len(weights)
    dp = create_matrix(n, capacity)
    fillFirstRow(dp, profits[0], weights[0], capacity)
    for i in range(1, n):
        for j in range(1, capacity + 1):
            left = dp[i][j - 1]
            up = dp[i-1][j]
            c = j - weights[i]
            include_obj = 0 if c < 0 else dp[i - 1][c] + profits[i]
            dp[i][j] = max(left, up, include_obj)
    return dp[-1][-1]


def create_matrix(n, capacity):
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n)]
    return dp


def fillFirstRow(dp, profit1, weight1, capacity):
    # Fill in first row
    for i in range(weight1, capacity + 1):
        dp[0][i] = profit1


profits1 = [60, 100, 120]
weights1 = [10, 20, 30]
max_capacity1 = 50
print(knapsack_0_1(profits1, weights1, max_capacity1))

profits2 = [60, 50, 70, 30]
weights2 = [5, 3, 4, 2]
max_capacity2 = 5

profits3 = [2, 3, 1, 4]
weights3 = [3, 4, 6, 5]
max_capacity3 = 8
