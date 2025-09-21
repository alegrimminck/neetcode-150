class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def backtrack(i):
            if i == len(s):
                res.append(path.copy())
                return
            
            for j in range(i, len(s)):
                if not self.isPali(s[i:j+1]):
                    continue
                
                path.append(s[i:j+1])
                backtrack(j+1)
                path.pop()
        
        backtrack(0)
        return res
    
    def isPali(self, word):
        l, r = 0, len(word)-1

        while l < r:
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1
        return True
            