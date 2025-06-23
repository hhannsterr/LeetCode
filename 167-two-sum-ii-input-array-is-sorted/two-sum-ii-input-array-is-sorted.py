class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(numbers):
            diff = target - num
            if num in hash_map:
                return [hash_map[num], i+1]
            else:
                hash_map[target - num] = i+1
