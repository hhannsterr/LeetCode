class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0:
            return []
        if n == 1:
            return [str(nums[0])]
        
        start = 0
        i = 0
        j = 1
        output = []
        while j < n:
            if nums[j] == nums[i] + 1:
                i += 1
            else:
                if i == start:
                    output.append(str(nums[start]))
                else:
                    output.append(f'{nums[start]}->{nums[i]}')
                start = j
                i = j
            
            j += 1

        if start == i:
            output.append(str(nums[start]))
        else:
            output.append(f'{nums[start]}->{nums[i]}')
        
        return output
