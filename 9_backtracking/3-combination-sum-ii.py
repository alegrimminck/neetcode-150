class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        result = []
        path = []

        def dfs(i, total):
            if total == target:
                result.append(path.copy())
                return
            
            if total > target or i >= len(candidates):
                return
            
            path.append(candidates[i])
            dfs(i+1, total+candidates[i])                
            path.pop()

            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, total)

        dfs(0,0)
        return result
