public int coinChange(int[] coins, int amount) {
    int[] dp = new int[amount + 1];
    Arrays.fill(dp, Integer.MAX_VALUE);
    dp[0] = 0;
    
    for (int i = 1; i <= amount; i++) {
        for (int coin : coins) {
            if (coin <= i && dp[i - coin] != Integer.MAX_VALUE) {
                dp[i] = Math.min(dp[i], dp[i - coin] + 1);
            }
        }
    }
    
    return dp[amount] == Integer.MAX_VALUE ? -1 : dp[amount];
}

//First, we create a dynamic programming array dp of size amount + 1 to store the minimum number of coins needed to make up each amount from 0 to amount.
//We initialize all elements of dp array with Integer.MAX_VALUE except dp[0], which is set to 0, since it requires 0 coins to make up amount 0. 
//Next, we iterate through amounts from 1 to amount and for each amount, we iterate through each coin denomination in the coins array. 
//For each coin denomination, if the current coin can be used to make up the current amount (coin <= i) and using this coin results in a smaller number of coins than the current value in dp[i]. 
//We update dp[i] with the minimum number of coins. 
//We then return dp[amount], which is the minimum number of coins needed to make up the given amount. If it's still Integer.MAX_VALUE, it means the amount cannot be made up, so we return -1.
