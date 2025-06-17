class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def get_int(n):
            return ord(n) - 48
        
        def convert_to_int(num):
            output = 0
            for n in num:
                output = output*10 + get_int(n)
            return output
                
        output = convert_to_int(num1) * convert_to_int(num2)
        return str(output)
