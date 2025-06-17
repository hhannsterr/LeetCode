class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = len(nums) - 1
        while i > 1:
            if nums[i] == nums[i-2]:
                nums.pop(i)
            i -= 1
    