class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        full_set = set(list(range(len(nums) + 1)))
        return full_set.difference(set(nums)).pop()
