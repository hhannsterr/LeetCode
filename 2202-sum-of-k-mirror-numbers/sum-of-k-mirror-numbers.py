class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def gen_palindrome_base() -> tuple[List[int], List[int]]:
            p_1 = [str(i) for i in range(10)]
            p_2 = [p_1[i]*2 for i in range(1, len(p_1))]
            return p_1, p_2

        def gen_palindrome(decimal_place: int, p_prev: List[int], p_1: List[int], p_2: List[int]) -> List[int]:
            output = []
            if decimal_place % 2 == 1:
                mid = decimal_place
                palindrome = p_1

            else:
                mid = decimal_place - 1
                palindrome = p_2.copy()
                palindrome.insert(0, '00')

            mid = mid // 2
            for prev in p_prev:
                front = prev[:mid]
                back = prev[mid:]
                for p in palindrome:
                    output.append(front+p+back)
            
            return output
                
        def is_palindrome(string: str) -> bool:
            return string == string[::-1]

        def to_base_k(num: int, k=k) -> str:
            whole, remain = num // k, num % k
            output = str(remain)
            while whole != 0:
                whole, remain = whole // k, whole % k
                output = str(remain) + output

            return output

        def check(p_arr: List[int], amount: int, total: int, k=k, n=n) -> tuple[int, int]:
            for p in p_arr:
                
                num = int(p)
                base_k = to_base_k(num, k)
                if is_palindrome(base_k):
                    amount += 1
                    total += num
                    print(num, base_k, total)

                if amount == n:
                    break
            
            return total, amount

        
        if n == 1:
            return n

        p_1, p_2 = gen_palindrome_base()
        
        p_1_2 = p_1 + p_2
        p_1_2.pop(0)
        
        total, amount = check(p_1_2, 0, 0)

        if amount == n:
            return total
        
        counter = 3
        p_prev = p_2
        while amount < n:
            p_counter = gen_palindrome(counter, p_prev, p_1, p_2)
            total, amount = check(p_counter, amount, total)

            if amount == n:
                return total

            p_counter = gen_palindrome(counter+1, p_prev, p_1, p_2)
            total, amount = check(p_counter, amount, total)

            if amount == n:
                return total

            p_prev = p_counter
            counter += 2
