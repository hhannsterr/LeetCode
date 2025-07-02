class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        elif n == 1:
            return [0, 1]

        prev_count = [0, 1]
        
        while len(prev_count) <= n // 2:
            prev_count += [x+1 for x in prev_count]
        
        remain = n + 1 - len(prev_count)
        prev_count += [x+1 for x in prev_count[:remain]]

        return prev_count
