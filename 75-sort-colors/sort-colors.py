class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr_0 = []
        arr_1 = []
        
        for num in nums:
            if num == 0:
                arr_0.append(num)
            elif num == 1:
                arr_1.append(num)
        
        len_0 = len(arr_0)
        len_0_1 = len_0 + len(arr_1)
        len_2 = len(nums[ len_0_1 : ])
        
        nums[ : len_0] = arr_0
        nums[ len_0 : len_0_1 ] = arr_1
        nums[ len_0_1 : ] = [2]*len_2
