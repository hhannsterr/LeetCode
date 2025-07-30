class Solution:
    def longestSubarray(self, nums: List[int]) -> int:       
        maximum = max(nums)
        output = 0
        count = 0
        for num in nums:
            if num == maximum:
                count += 1
            else:
                output = max(output, count)
                count = 0
        
        output = max(output, count)
        return output
