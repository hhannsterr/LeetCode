class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for index, val in enumerate(nums):
            if target - val in hash_map:
                return index, hash_map[target - val]
            else:
                hash_map[val] = index