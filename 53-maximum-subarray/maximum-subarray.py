class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        found = False
        for i in range(len(nums)):
            if nums[i] > 0:
                dp = [nums[i]]
                index = i
                found = True
                break
        
        if not found:
            return max(nums)
        
        max_right_now = 0
        for i in range(index+1, len(nums)):
            if dp[-1] <= 0:
                max_right_now = max(max_right_now, max(dp))
                dp = [nums[i]]
            else:
                dp.append(dp[-1] + nums[i])
        
        return max(max_right_now, max(dp))
        