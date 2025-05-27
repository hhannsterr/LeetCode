class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def check(i, prev_sum):
            if prev_sum == target:
                RESULT.append(CURRENT.copy())
            elif prev_sum < target:
                for j in range(i, len(candidates)):
                    CURRENT.append(candidates[j])
                    check(j, prev_sum + candidates[j])
                    CURRENT.pop()
            return RESULT

        CURRENT = []
        RESULT = []

        return check(0, 0)
