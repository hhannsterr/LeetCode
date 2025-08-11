class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def get_powers(binary_num: str) -> List[int]:
            value = 1
            power = []
            for num in binary_num[::-1]:
                if num == '1':
                    power.append(value)
                value *= 2
            return power

        def get_prefix(powers: List[int], length: int) -> List[int]:
            prefix = [1]
            for power in powers:
                prefix.append(power * prefix[-1])
            return prefix[1:]

        def mod(answer: int) -> int:
            return answer % (10**9 + 7)


        binary_num = bin(n)[2:]
        powers = get_powers(binary_num)

        len_prefix = queries[-1][-1] + 1
        prefix = get_prefix(powers, len_prefix)

        answers = []
        for left, right in queries:
            if left == 0:
                answers.append(mod(prefix[right]))
            else:
                ans = prefix[right] // prefix[left-1]
                answers.append(mod(ans))

        return answers
