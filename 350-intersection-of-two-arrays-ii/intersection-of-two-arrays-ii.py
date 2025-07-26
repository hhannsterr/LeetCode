class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def get_hash_map(nums):
            hash_map = {}
            for num in nums:
                if num in hash_map:
                    hash_map[num] += 1
                else:
                    hash_map[num] = 1
            return hash_map

        def check(h_short, h_long):
            output = []
            for num, amount in h_short.items():
                if num in h_long:
                    freq = min(amount, h_long[num])
                    for time in range(freq):
                        output.append(num)
            return output


        hash_map1 = get_hash_map(nums1)
        hash_map2 = get_hash_map(nums2)

        if len(hash_map1) < len(hash_map2):
            return check(hash_map1, hash_map2)
        else:
            return check(hash_map2, hash_map1)