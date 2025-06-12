class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        def mad(num1, num2):
            return abs(num1 - num2)
        
        maximum = mad(nums[0], nums[-1])
        prev = nums[0]
        for num in nums[1:]:
            diff = mad(num, prev)
            if diff > maximum:
                maximum = diff
            prev = num
        
        return maximum
