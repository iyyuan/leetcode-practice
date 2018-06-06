import math

class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        # Initialize the number of ways for all amounts from 1-amount to inf
        min_ways = [math.inf] * (amount+1)
        # Base case is 0
        min_ways[0] = 0

        for coin in coins:
            for i in range(coin, amount+1):
                # If we subtract a coin from the current amount, and the minimum
                # number of ways to make that new amount plus one is less
                # then the current minimum number of ways to make change for
                # the current amount, we set the mininum number of ways to be
                # equal to the min number of ways to make change for
                # min_ways[i-coin] + 1, to account for a coin being added
                if min_ways[i-coin]+1 < min_ways[i]:
                    min_ways[i] = min_ways[i-coin]+1

        if min_ways[amount] == math.inf:
            return -1
        return min_ways[amount]
