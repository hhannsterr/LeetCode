class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        def check_state(curr, post):
            if curr == post:
                return 'e' # equal
            elif curr > post:
                return 'v' # valley
            else:
                return 'h' # hill


        for i in range(1, len(nums)):
            prev_state = check_state(nums[i-1], nums[i])
            if prev_state != 'e':
                start_index = i
                break

        if prev_state == 'e':
            return 0
            
        output = 0
        for i in range(start_index, len(nums)-1):
            state = check_state(nums[i], nums[i+1])
            if state == 'e':
                continue
            if prev_state != state:
                output += 1
            prev_state = state
        
        return output

