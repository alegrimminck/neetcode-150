class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.isWord = True
        
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        res = set()

        def dfs(r, c, curr, word):
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r,c) in visited or
                board[r][c] not in curr.children):
                return
            
            char = board[r][c]
            visited.add((r,c))
            word += char
            curr = curr.children[char]

            if curr.isWord:
                res.add(word)
            
            dfs(r+1, c, curr, word)
            dfs(r-1, c, curr, word)
            dfs(r, c+1, curr, word)
            dfs(r, c-1, curr, word)

            visited.remove((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        return list(res)
            