class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        profit = 0
        max_profit = 0
        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r
            max_profit = max(profit, max_profit)

        return max_profit