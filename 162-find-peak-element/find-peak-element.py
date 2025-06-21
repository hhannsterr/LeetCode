class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def is_peak(nums, i):
            if i-1 < 0:
                return True
            return nums[i] > nums[i-1]

        
        length = len(nums)-1
        
        i = 1
        while i < length:
            if nums[i] > nums[i-1]:
                if nums[i] > nums[i+1]:
                    return i
            else:
                if is_peak(nums, i-1):
                    return i-1
            i += 2

        if is_peak(nums, length):
            return length    
        if is_peak(nums, length-1):
            return length-1 
