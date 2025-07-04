class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = n - (k % n)

        nums[k:], nums[:k] = nums[:k], nums[k:]
