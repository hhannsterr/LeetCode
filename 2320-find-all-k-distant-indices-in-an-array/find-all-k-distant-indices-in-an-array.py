class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        indexes = []
        for i, num in enumerate(nums):
            if num == key:
                indexes.append(i)

        output = []
        for i in range(len(nums)):
            for index in indexes:
                if abs(i - index) <= k:
                    output.append(i)
                    break
        
        return output
