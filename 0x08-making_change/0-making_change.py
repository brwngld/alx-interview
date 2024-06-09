def makeChange(coins, total):
    if total <= 0:
        return 0

    # Sort coins to try larger denominations first, which may lead to fewer steps
    coins.sort(reverse=True)

    # Initialize dp array with a large value (float('inf')), meaning not reachable
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: no coins needed to make a total of 0

    for coin in coins:
        for amount in range(coin, total + 1):
            if dp[amount - coin] + 1 < dp[amount]:
                dp[amount] = dp[amount - coin] + 1

    return dp[total] if dp[total] != float('inf') else -1