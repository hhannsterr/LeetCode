class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        answers = []
        total_num = 0
        for num in nums:
            total_num = (total_num * 2) + num
            answer = total_num % 5
            answers.append(answer == 0)

        return answers
