class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < cheapest:
                cheapest = prices[i]
            else:
                profit = prices[i] - cheapest
                if max_profit < profit:
                    max_profit = profit
        return max_profit
        