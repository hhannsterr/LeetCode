class Solution:
    def intToRoman(self, num: int) -> str:
        def roman(position, number):
            return d[position].get(number)
        
        d = {
            'unit': {
                '9': 'IX',
                '5': 'V',
                '4': 'IV',
                '1': 'I'
            },
            'tenth': {
                '9': 'XC',
                '5': 'L',
                '4': 'XL',
                '1': 'X'
            },
            'hundred': {
                '9': 'CM',
                '5': 'D',
                '4': 'CD',
                '1': 'C'
            },
            'thousand': {
                '1': 'M'
            }
        }

        string_num = str(num)
        num_position = ['unit', 'tenth', 'hundred', 'thousand']
        output = ''
        for num, pos in zip(string_num[::-1], num_position):
            letter = roman(pos, num)
            if letter:
                output = letter + output
            else:
                if num < '5':
                    times = int(num)
                    output = roman(pos, '1') * times + output
                else:
                    times = int(num) - 5
                    output = roman(pos, '5') + roman(pos, '1') * times + output
        
        return output
