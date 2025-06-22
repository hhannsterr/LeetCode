class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        track = 0
        output = []
        while track < len(s):
            output.append(s[track:track+k])
            track += k

        length_last = len(output[-1])
        if length_last < k:
            fill_amount = k - length_last
            output[-1] += fill * fill_amount

        return output
