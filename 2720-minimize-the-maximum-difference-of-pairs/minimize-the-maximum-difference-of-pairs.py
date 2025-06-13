class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        
        def get_mid(high, low):
            return (high + low) // 2

        def check(mid):
            i = 1
            count = 0
            while i < len(nums):
                if (nums[i] - nums[i-1]) <= mid:
                    count += 1
                    i += 1
                i += 1
            return count


        if p == 0:
            return 0

        nums.sort()
        
        high = nums[-1] - nums[0]
        low = 0

        while low < high:
            mid = get_mid(high, low)
            if check(mid) >= p:
                high = mid
            else:
                low = mid + 1
        return low
