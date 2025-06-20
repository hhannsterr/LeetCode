class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def tmr_decreases(today, tmr):
            return today > tmr
        

        bought = False
        profit = 0
        today = prices[0]
        for i in range(1, len(prices)):
            tmr = prices[i]
            if bought:
                if tmr_decreases(today, tmr):
                    profit += today - price_bought
                    bought = False
            else:
                if not tmr_decreases(today, tmr):
                    price_bought = today
                    bought = True
            today = tmr

        if bought:
            profit += today - price_bought
        
        return profit



