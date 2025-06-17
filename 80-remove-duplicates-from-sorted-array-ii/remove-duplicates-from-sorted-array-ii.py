class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = nums[0]
        cnt = 1
        to_pop = []
        for i in range(1, len(nums)):
            if nums[i] == temp:
                cnt += 1
            else:
                temp = nums[i]
                cnt = 1
            if cnt > 2:
                to_pop.append(i)
        
        for i in to_pop[::-1]:
            nums.pop(i)
