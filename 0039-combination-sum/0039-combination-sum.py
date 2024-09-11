from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(remaining, combination, start):
            if remaining == 0:
                # If we hit the target, add the current combination to the results
                results.append(list(combination))
                return
            elif remaining < 0:
                # If we exceed the target, no need to continue exploring
                return
            
            for i in range(start, len(candidates)):
                # Include the candidate
                combination.append(candidates[i])
                # Continue exploring with the same candidate
                backtrack(remaining - candidates[i], combination, i)
                # Backtrack, remove the last candidate
                combination.pop()
        
        results = []
        backtrack(target, [], 0)
        return results