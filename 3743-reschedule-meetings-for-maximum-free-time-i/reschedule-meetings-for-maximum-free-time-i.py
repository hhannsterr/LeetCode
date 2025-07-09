class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        freeTime = [startTime[0]]
        for start, end in zip(startTime[1:], endTime):
            freeTime.append(start - end)
        freeTime.append(eventTime - endTime[-1])

        prev = freeTime[0]
        output = sum(freeTime[:k+1])
        for i in range(1, len(freeTime) - k):
            window = i + k
            if freeTime[window] > prev:
                output = max(output, sum(freeTime[ i : window + 1 ]))
            prev = freeTime[i]
        
        return output
