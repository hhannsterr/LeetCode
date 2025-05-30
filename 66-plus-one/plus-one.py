class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        def add(addition):
            if addition == 10:
                return 1, 0
            else:
                return 0, addition
        
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            if carry == 1:
                carry, digits[i] = add(digits[i] + carry)
            else:
                break
        
        if carry == 1:
            return [1] + digits

        return digits
