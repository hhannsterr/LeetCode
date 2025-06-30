class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        def check(arr):
            temp = 0
            for index, value in enumerate(arr):
                temp += value
                if temp < 0:
                    return False, index
            return True, index
        
        profit = []
        for g, c in zip(gas, cost):
            profit.append(g - c)
        
        if sum(profit) < 0:
            return -1
        i = 0
        while i < len(profit):
            if profit[i] < 0:
                i += 1
                continue
            temp = profit[i:] + profit[:i]
            found, index = check(temp)
            if found:
                return i
            else:
                i += index
