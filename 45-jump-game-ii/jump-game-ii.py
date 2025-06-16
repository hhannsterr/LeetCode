class Solution:
    def jump(self, nums: List[int]) -> int:
        to_reach = len(nums) - 1
        dp = [len(nums)] * to_reach
        for i in range(len(nums)-2, -1, -1):
            can_reach = nums[i] + i
            if can_reach >= to_reach:
                dp[i] = 1
            else:
                if nums[i] != 0:
                    dp[i] = 1 + min(dp[i+1: can_reach+1])
        
        if dp == []:
            return 0
        return dp[0]
        