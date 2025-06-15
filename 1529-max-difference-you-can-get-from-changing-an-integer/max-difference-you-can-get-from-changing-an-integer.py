class Solution:
    def maxDiff(self, num: int) -> int:
        def found(to_replaced):
            return to_replaced != ''

        def is_number(s, number):
            return s == number
        
        def replace(string, number):
            output = ''
            to_replaced = ''
            first = True
            check = number
            for s in string:
                if first and is_number(check, '1'):
                    if is_number(s, '1'):
                        output += '1'
                        number = '0'
                    elif is_number(s, '0'):
                        output += '0'
                    else:
                        to_replaced = s
                        output += number
                        first = False
                    continue

                if found(to_replaced):
                    if is_number(s, to_replaced):
                        output += number
                    else:
                        output += s
                else:
                    if not is_number(s, number):
                        to_replaced = s
                        output += number
                    else:
                        output += s
            
            return output

        num = str(num)
        maximum = int(replace(num, '9'))
        minimum = int(replace(num, '1'))
        return maximum - minimum
