class Solution:
    def minMaxDifference(self, num: int) -> int:
        def found(to_replaced):
            return to_replaced == ''

        def is_number(to_check, number):
            return to_check == number

        def replace_number(string, number):
            temp = ''
            to_replaced = ''
            for i in range(len(string)):
                if found(to_replaced):    
                    if not is_number(string[i], number):
                        to_replaced = string[i]
                        temp += number
                    else:
                        temp += string[i]
                else:
                    if is_number(string[i], to_replaced):
                        temp += number
                    else:
                        temp += string[i]
            
            return temp
        

        num = str(num)
        maximum = int(replace_number(num, '9'))
        minimum = int(replace_number(num, '0'))
        
        return maximum - minimum
        