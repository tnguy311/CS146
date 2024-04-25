def coinChange(self, coins: List[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

*Similar to the Java implementation, we create a dynamic programming list dp of size amount + 1 to store the minimum number of coins needed to make up each amount from 0 to amount. We initialize all elements of dp list with float('inf') except dp[0], which is set to 0. Then we iterate through amounts from 1 to amount and for each amount, we iterate through each coin denomination in the coins list. For each coin denomination, if the current coin can be used to make up the current amount (coin <= i) and using this coin results in a smaller number of coins than the current value in dp[i], we update dp[i] with the minimum number of coins. Finally, we return dp[amount] if it's not float('inf'), which represents the minimum number of coins needed to make up the given amount. If it's still float('inf'), it means the amount cannot be made up, so we return -1. 
