class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        
        output = []
        for i in range(0, len(nums), 3):
            batch = nums[i:i+3]
            if batch[-1] - batch[0] > k:
                return []
            else:
                output.append(batch)
        
        return output
