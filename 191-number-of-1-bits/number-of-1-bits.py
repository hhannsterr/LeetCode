class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_string = bin(n)[2:]
        output = 0
        for letter in binary_string:
            if letter == '1':
                output += 1
        return output
