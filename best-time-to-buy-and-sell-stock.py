class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        # Used to keep track of the global min
        # as we find it
        lowest_so_far = prices[0]
        profit = 0

        for i, v in enumerate(prices):
            if i == 0:
                continue

            if v < lowest_so_far:
                # Update the global min as we find it
                lowest_so_far = v
            else:
                # Compute the max profit for every entry
                # as the max of the current profit and the
                # current stock price - the global min
                profit = max(profit, v - lowest_so_far)

        return profit
