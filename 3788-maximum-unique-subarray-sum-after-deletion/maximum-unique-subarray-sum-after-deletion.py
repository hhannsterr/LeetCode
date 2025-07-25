class Solution:
    def maxSum(self, nums: List[int]) -> int:
        set_num = set()
        for num in nums:
            if num <= 0:
                continue
            if num not in set_num:
                set_num.add(num)
        
        if set_num:
            return sum(set_num)
        return max(nums)
