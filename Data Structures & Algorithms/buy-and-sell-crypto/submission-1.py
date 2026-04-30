class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            diff = prices[i] - min_price
            if diff > max_profit:
                max_profit = diff
        return max_profit