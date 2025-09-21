class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
            
        digitMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        path = []

        def backtrack(i):
            if i == len(digits):
                res.append("".join(path))
                return
            
            for digit in digitMap[digits[i]]:
                path.append(digit)
                backtrack(i+1)
                path.pop()
        
        backtrack(0)
        return res