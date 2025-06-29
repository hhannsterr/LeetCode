class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        if n < 2:
            return

        i = 0
        z_index = 0
        count_zero = 0
        count_loop = 0
        first_zero = False
        
        while count_loop < n:
            if nums[i] == 0:
                if not first_zero:
                    z_index = i
                first_zero = True
                i += 1
                count_zero += 1
            else:
                if first_zero:
                    batch = nums[i:]
                    nums[z_index:z_index+len(batch)] = batch
                    i = z_index + 1
                else:
                    i += 1
                first_zero = False

            count_loop += 1

        if count_zero != 0:
            nums[-count_zero:] = [0] * count_zero
        
                
