from types import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        for row in board:
            if not self.isValid(row):
                return False
        
        # columns
        columns = zip(*board)
        for column in columns:
            if not self.isValid(column):
                return False
        
        # boxes
        for iniI in range(0, 9, 3):
            for iniJ in range(0, 9, 3):
                l = []
                for i in range(iniI, iniI+3):
                    for j in range(iniJ, iniJ+3):
                        l.append(board[i][j])
                if not self.isValid(l):
                    return False

        return True

        
    def isValid(self, l):
        hashSet = set()
        for n in l:
            if n != ".":
                if n in hashSet:
                    return False
                hashSet.add(n)
        return True
