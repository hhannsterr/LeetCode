class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        if len(word) <= 2:
            return 0

        freq = {}
        for letter in word:
            if letter in freq:
                freq[letter] += 1
            else:
                freq[letter] = 1

        freq = list(freq.values())
        if len(freq) < 2:
            return 0
        freq.sort()

        output = 100000
        delete = 0
        for i in range(0, len(freq)-1):
            if freq[i] == freq[i-1]:
                delete += freq[i]
                continue
            
            thres = freq[i]+k
            total = 0
            for j in range(i+1, len(freq)):
                if freq[j] > thres:
                    total += freq[j] - thres
            
            total += delete
            delete += freq[i]

            output = min(output, total)
        
        if freq[-1] == freq[-2]:
            if output == 100000:
                return 0
            else:
                return output
        else:
            return min(output, delete)

        # freq.sort()

        # thres_min = freq[0] + k
        # thres_max = freq[-1] - k

        # min_amount = bsa(freq, thres_min, 0, len(freq))
        # max_amount = bsa(freq, thres_max, 0, len(freq))
        # print(min_amount, max_amount)
        # print(f'min: {freq[min_amount+1:]}')
        # print(f'max: {freq[:max_amount]}')
        # print(freq)
