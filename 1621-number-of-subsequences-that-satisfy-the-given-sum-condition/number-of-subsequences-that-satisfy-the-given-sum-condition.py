class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        def binary_search(arr, target, start, end):
            if start > end:
                return start-1
            mid = (start + end) // 2
            if arr[mid] > target:
                return binary_search(arr, target, start, mid-1)
            else:
                return binary_search(arr, target, mid+1, end)

        
        MOD = 10**9 + 7
        
        nums.sort()

        count = 0
        for i in range(len(nums)):
            target_j = target - nums[i]
            j = binary_search(nums, target_j, i, len(nums)-1)
            if i > j:
                break
            count += pow(2, j - i)
            
        return count % MOD
