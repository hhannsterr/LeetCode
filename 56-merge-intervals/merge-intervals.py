class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def check_merge(stack, output):
            if len(stack) == 1:
                output.append(stack.pop())
                return stack, output
            start_0, end_0 = stack[0]
            start_1, end_1 = stack[1]
            if end_0 >= start_1:
                end_0 = max(end_0, end_1)
                new_stack = [[start_0, end_0]]
            else:
                new_stack = [[start_1, end_1]]
                output.append([start_0, end_0])

            return new_stack, output
        
        
        if len(intervals) == 1:
            return intervals
        
        intervals.sort(key = lambda x: x[0], reverse=True)
        
        stack = []
        output = []
        
        while len(stack) != 0 or len(intervals) != 0:
            if len(stack) != 2 and len(intervals) != 0:
                stack.append(intervals.pop())
            else:
                stack, output = check_merge(stack, output)

        return output
