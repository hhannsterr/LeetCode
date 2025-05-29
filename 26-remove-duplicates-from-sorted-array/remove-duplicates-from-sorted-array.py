class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = nums[0]
        index = 1
        for i in range(1, len(nums)):
            if nums[i] != temp:
                temp, nums[index] = nums[i], nums[i]
                index += 1
        
        del nums[index:]
