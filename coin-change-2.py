class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        num_ways = [0] * (amount + 1)
        num_ways[0] = 1

        for coin in coins:
            for i in range(coin, amount+1):
                num_ways[i] += num_ways[i-coin]

        return num_ways[amount]
