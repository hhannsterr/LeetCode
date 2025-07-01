class Solution:
    def findMin(self, nums: List[int]) -> int:
        def binary_search(arr, start, end):
            if start > end:
                return arr[start]
            
            mid = (start + end) // 2

            if arr[mid] > arr[end]:
                new_start = mid+1
                if arr[mid] > arr[new_start]:
                    return arr[new_start]
                else:
                    return binary_search(arr, new_start, end)
            
            elif arr[mid] < arr[start]:
                new_end = mid-1
                if arr[mid] < arr[new_end]:
                    return arr[mid]
                else:
                    return binary_search(arr, start, new_end)
            
            elif arr[mid] < arr[end] and arr[mid] > arr[start]:
                return arr[mid]
        

        if nums[0] <= nums[-1]:
            return nums[0]

        return binary_search(nums, 0, len(nums)-1)
