class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums)-2:
            if nums[i] == nums[i+2]:
                nums.pop(i)
            else:
                i += 1
        # i = len(nums) - 1
        # while i > 1:
        #     if nums[i] == nums[i-2]:
        #         nums.pop(i)
        #     i -= 1
        # temp = nums[0]
        # cnt = 1
        # to_pop = []
        # for i in range(1, len(nums)):
        #     if nums[i] == temp:
        #         cnt += 1
        #     else:
        #         temp = nums[i]
        #         cnt = 1
        #     if cnt > 2:
        #         to_pop.append(i)
        
        # for i in to_pop[::-1]:
        #     nums.pop(i)
