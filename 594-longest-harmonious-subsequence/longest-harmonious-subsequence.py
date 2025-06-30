class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        hash_map = {}
        for i, num in enumerate(nums):
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1

        max_sub = 0
        for key, val in hash_map.items():
            target = key - 1
            if target in hash_map:
                max_sub = max(max_sub, val + hash_map[target])

        return max_sub
