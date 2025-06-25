class Solution:
    def isHappy(self, n: int) -> bool:
        def happy(number):
            string = str(number)
            result = sum([int(s)**2 for s in string])
            print(result)
            if result == 1 or result == 7:
                return True
            elif result > 9:
                return happy(result)
            else:
                return False

                   
        return happy(n)
