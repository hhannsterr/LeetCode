class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def binary_search(arr, new_val, start, end):
            if start >= end:
                val = arr[start]
                if val[0] == new_val[0]:
                    if val[1] >= new_val[1]:
                        return start
                    else:
                        return start + 1
                elif val[0] > new_val[0]:
                    return start
                else:
                    return start + 1
                    
            mid = (start + end) // 2
            val = arr[mid]
            if val[0] == new_val[0]:
                if val[1] >= new_val[1]:
                    return mid
                else:
                    return mid + 1
            elif val[0] < new_val[0]:
                return binary_search(arr, new_val, mid+1, end)
            else:
                return binary_search(arr, new_val, start, mid-1)


        if intervals == []:
            return [newInterval]

        index = binary_search(intervals, newInterval, 0, len(intervals)-1)
        output = []
        
        new_start, new_end = newInterval[0], newInterval[1]
        if index != 0:
            start, end = intervals[index-1][0], intervals[index-1][1]
            if end >= new_start:
                if end >= new_end:
                    return intervals
                else:
                    new_start = start
                    output += intervals[:index-1]
            else:
                output += intervals[:index]
        
        if index == len(intervals):
            return output + [[new_start, new_end]]

        for i in range(index, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if new_end >= start:
                if new_end <= end:
                    output += [[new_start, end]]
                    return output + intervals[i+1:]
            else:
                output += [[new_start, new_end]]
                return output + intervals[i:]
            
        return output + [[new_start, new_end]]

        