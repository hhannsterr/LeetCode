class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_sum = 0
        current_sum = 0
        num_set = set()
        left = 0

        for num in nums:
            if num in num_set:
                while nums[left] != num:
                    current_sum -= nums[left]
                    num_set.remove(nums[left])
                    left += 1            
                
                left += 1
            else:
                num_set.add(num)
                current_sum += num
                max_sum = max(max_sum, current_sum)                    

        return max_sum
