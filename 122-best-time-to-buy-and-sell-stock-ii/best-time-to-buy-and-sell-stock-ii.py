class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def tmr_increases(today, tmr):
            return today < tmr
        

        profit = 0
        for i in range(1, len(prices)):
            if tmr_increases(prices[i-1], prices[i]):
                profit += prices[i] - prices[i-1]
        
        return profit



