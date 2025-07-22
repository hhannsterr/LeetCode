class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        output = 0
        start = 0
        hash_map = {}
        for i, num in enumerate(nums):
            if num in hash_map:
                if start > hash_map[num]:
                    hash_map[num] = i
                else:
                    output = max(output, sum(nums[start:i]))
                    start = hash_map[num]+1
                    hash_map[num] = i
            else:
                hash_map[num] = i

        output = max(output, sum(nums[start:]))
        
        return output
