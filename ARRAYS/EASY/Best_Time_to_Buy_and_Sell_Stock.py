"""
121. Best Time to Buy and Sell Stock  -- DP

Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
        profit =0
        min_price=prices[0]
        for i in range(1,len(prices)):
            profit = max(profit, prices[i] - min_price)
            min_price = min(prices[i],min_price)

        return profit