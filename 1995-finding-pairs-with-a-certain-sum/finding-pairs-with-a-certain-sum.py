class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        def gen(nums):
            hash_map = {}
            for num in nums:
                if num in hash_map:
                    hash_map[num] += 1
                else:
                    hash_map[num] = 1
            return hash_map

        self.nums1 = gen(nums1)
        self.nums2 = gen(nums2)
        self.arr2 = nums2

    def add(self, index: int, val: int) -> None:
        num = self.arr2[index]
        self.arr2[index] += val
        if num in self.nums2:
            self.nums2[num] -= 1
        
        new_num = num + val
        if new_num in self.nums2:
            self.nums2[new_num] += 1
        else:
            self.nums2[new_num] = 1

    def count(self, tot: int) -> int:
        count = 0
        for num, amount in self.nums1.items():
            target = tot - num
            if target in self.nums2:
                count += amount * self.nums2[target]
        return count




# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)