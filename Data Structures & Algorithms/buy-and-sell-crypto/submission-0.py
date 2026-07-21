class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = 0
        for i in range(1, len(prices)):
            if prices[buy] > prices[i]:
                buy = i
            else:
                max_profit = max(prices[i]-prices[buy], max_profit)
        return max_profit
