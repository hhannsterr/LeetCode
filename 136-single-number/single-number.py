class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dictionary = {}
        for num in nums:
            if num in dictionary:
                dictionary.pop(num)
            else:
                dictionary[num] = 1
        return list(dictionary.keys())[0]
        