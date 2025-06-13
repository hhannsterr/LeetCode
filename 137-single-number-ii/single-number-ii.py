class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_map = {}
        for num in nums:
            if hash_map.get(num):
                hash_map[num] += 1
                if hash_map[num] == 3:
                    hash_map.pop(num)
            else:
                hash_map[num] = 1
        
        return next(iter(hash_map))
