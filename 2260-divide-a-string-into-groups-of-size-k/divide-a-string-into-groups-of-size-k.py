class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        output = []
        for track in range(0, len(s), k):
            output.append(s[track:track+k])

        length_last = len(output[-1])
        if length_last < k:
            fill_amount = k - length_last
            output[-1] += fill * fill_amount

        return output
