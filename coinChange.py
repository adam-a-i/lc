class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # dp[i] = minimum number of coins to make amount i
        # initialize with amount+1 (impossible / infinity placeholder)
        dp = [amount + 1] * (amount +1) 
        dp[0] = 0
 # We loop through every amount 1..amount
        # because "amt" represents all possible remainders we can get
        # after subtracting coins step by step (not just the coin values themselves).
        for amt in range(1, amount + 1):
            for c in coins:
                if amt - c >= 0:
                    # if we use coin c, then the problem reduces to amt - c
                    dp[amt] = min(dp[amt], 1 + dp[amt-c])

        return dp[amount] if dp[amount] != amount + 1 else -1
