class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []
        for i in s:
            if i in {'(', '[', '{'}:
                stack.append(i)
            else:
                if stack == []:
                    return False
                if i != hash_map[stack.pop()]:
                    return False
        if stack != []:
            return False
        return True
