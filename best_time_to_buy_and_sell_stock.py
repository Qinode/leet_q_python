class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        else:
            max_profit = 0
            min_price = prices[0]
            for i in range(1, len(prices)):
                if prices[i] - min_price > max_profit:
                    max_profit = prices[i] - min_price

                if prices[i] < min_price:
                    min_price = prices[i]
        return max_profit