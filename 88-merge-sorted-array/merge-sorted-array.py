class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if nums2 == []:
            return
        
        i = m-1
        j = n-1

        for index in range(m+n-1, -1, -1):
            if j < 0:
                nums1[index] = nums1[i]
                i -= 1
                continue
            if i < 0:
                nums1[index] = nums2[j]
                j -= 1
                continue
            if nums2[j] > nums1[i]:
                nums1[index] = nums2[j]
                j -= 1
            else:
                nums1[index] = nums1[i]
                i -= 1
        