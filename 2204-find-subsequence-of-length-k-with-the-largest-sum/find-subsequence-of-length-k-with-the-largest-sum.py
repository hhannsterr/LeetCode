class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        def sort(dictionary):
            return sorted(
                dictionary.items(), 
                key=lambda item: item[1], 
                reverse=True
            )
        
        hash_map = {}
        for index, num in enumerate(nums):
            hash_map[index] = num

        k_list = sort(hash_map)[:k]
        k_list.sort(key=lambda item: item[0])

        return [value for _, value in k_list]
