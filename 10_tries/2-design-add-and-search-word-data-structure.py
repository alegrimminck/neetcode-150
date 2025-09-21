class Node:

    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.isWord = True

    def search(self, word: str) -> bool:
        def dfs(i, curr):
            if i == len(word) and curr.isWord:
                return True
            
            if i == len(word):
                return False
            
            if word[i] == ".":
                for c in curr.children:
                    if dfs(i+1, curr.children[c]):
                        return True
                return False

            if word[i] not in curr.children:
                return False

            return dfs(i+1, curr.children[word[i]])

        return dfs(0, self.root)