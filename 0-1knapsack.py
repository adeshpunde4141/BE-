def knapSack(W, wt, val, n):
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - wt[i - 1]] + val[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][W]  

if __name__ == '__main__':
    n = int(input("Enter the number of items: "))
    profit = []
    weight = []
    for i in range(n):
        value = int(input(f"Enter value for item {i + 1}: "))
        weight_value = int(input(f"Enter weight for item {i + 1}: "))
        profit.append(value)
        weight.append(weight_value)
    W = int(input("Enter the capacity of the knapsack: "))
    max_value = knapSack(W, weight, profit, n)
    print(f"Maximum value in the knapsack = {max_value}")
