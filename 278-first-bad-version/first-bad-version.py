# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        def binary_search(start, end):
            if start > end:
                return
            
            mid = (start + end) // 2
            bad = isBadVersion(mid)
            
            if bad:
                new_end = mid-1
                if not isBadVersion(new_end):
                    return mid
                return binary_search(start, new_end)
            else:
                new_start = mid+1
                if isBadVersion(new_start):
                    return new_start
                return binary_search(new_start, end)

        return binary_search(1, n)
