class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        length = len(nums)
        max_right_now = -1
        output = -1
        for i in range(length-1, -1, -1):
            if nums[i] >= max_right_now:
                max_right_now = nums[i]
            else:
                output = max(output, max_right_now - nums[i])
            
        return output
