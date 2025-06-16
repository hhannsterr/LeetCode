class Solution:
    def canJump(self, nums: List[int]) -> bool:
        to_reach = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] + i >= to_reach:
                to_reach = i

        if to_reach == 0:
            return True
        else:
            return False
