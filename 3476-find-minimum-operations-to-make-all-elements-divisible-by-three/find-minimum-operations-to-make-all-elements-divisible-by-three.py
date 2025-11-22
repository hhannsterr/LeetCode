class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0
        for num in nums:
            remainder = num % 3
            if remainder == 0:
                cnt += 1
        return len(nums) - cnt
