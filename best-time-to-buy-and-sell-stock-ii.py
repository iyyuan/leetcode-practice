class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        local_min = prices[0]
        local_max = prices[0]
        prev = prices[0]
        profit = 0

        for i, v in enumerate(prices):
            if i == 0:
                continue

            # Only concerned with one of two cases
            # i)   the current price is greater than yesterdays
            # ii)  the current price is lower than yesterdays

            if v > prev:
                # Update the local max
                local_max = v
            elif v < prev:
                # A drop in stock price means two things:
                # i)  we should sell the day before
                # ii) we have a new local min, but we also need
                #     to update the local max going forward
                profit += local_max - local_min
                local_max = v
                local_min = v

            prev = v

        # Need this for edge case like [1, 2, 3, 4, 5]
        profit += local_max - local_min

        return profit
