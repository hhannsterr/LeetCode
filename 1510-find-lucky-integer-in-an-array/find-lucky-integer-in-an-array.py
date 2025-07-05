class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hash_map = {}
        for num in arr:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1

        output = -1
        for key, value in hash_map.items():
            if key == value:
                output = max(value, output)
        
        return output
        