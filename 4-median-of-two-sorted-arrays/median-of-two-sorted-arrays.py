class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def isEven(num):
            return num % 2 == 0
        
        def sort_odd(arr1, arr2, median):
            one, len1 = 0, len(arr1)
            two, len2 = 0, len(arr2)
            cnt = -1
            while one < len1 and two < len2:
                if arr1[one] <= arr2[two]:
                    temp = arr1[one]
                    one += 1
                else:
                    temp = arr2[two]
                    two += 1
                cnt += 1
                if cnt == median_location:
                    return temp

            if one < len1:
                return arr1[median - cnt + one - 1]
            else:
                return arr2[median - cnt + two - 1]

        def sort_even(arr1, arr2, median):
            def result(num1, num2):
                return (num1 + num2) / 2
            
            one, len1 = 0, len(arr1)
            two, len2 = 0, len(arr2)
            cnt = -1
            temp2 = 0
            while one < len1 and two < len2:
                if arr1[one] <= arr2[two]:
                    temp1, temp2 = temp2, arr1[one]
                    one += 1
                else:
                    temp1, temp2 = temp2, arr2[two]
                    two += 1
                cnt += 1
                if cnt == median_location:
                    return result(temp1, temp2)

            
            if one < len1:
                loc = median - cnt + one - 1
                if cnt == median - 1:
                    return result(temp2, arr1[loc])
                else:
                    return result(arr1[loc-1], arr1[loc])
            else:
                loc = median - cnt + two - 1
                if cnt == median - 1:
                    return result(temp2, arr2[loc])
                else:
                    return result(arr2[loc-1], arr2[loc])

        
        
        total_length = len(nums1) + len(nums2)
        median_location = total_length // 2
        
        if isEven(total_length):
            return sort_even(nums1, nums2, median_location)
        else:
            return sort_odd(nums1, nums2, median_location)
