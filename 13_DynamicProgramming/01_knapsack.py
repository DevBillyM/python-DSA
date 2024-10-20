# 0/1 Knapsack Problem using Dynamic Programming

def knapsack(values, weights, W, n):
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]

# Testing 0/1 Knapsack Problem
values = [60, 100, 120]
weights = [10, 20, 30]
W = 50
n = len(values)
print(f"Maximum value in Knapsack = {knapsack(values, weights, W, n)}")  # Output: 220
