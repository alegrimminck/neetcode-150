class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
            if endWord not in wordList:
                return 0
            
            adjList = defaultdict(list)
            for word in wordList:
                for option in wordList:
                    if option == word:
                        continue
                    if self.oneCharDiff(word, option):
                        adjList[word].append(option)
            

            def bfs(word):
                visited = set()
                visited.add(word)
                level = 1
                q = deque([word])
                while q:
                    level += 1
                    for _ in range(len(q)):
                        curr = q.popleft()
                        if curr == endWord:
                            return level

                        for nei in adjList[curr]:
                            if nei in visited:
                                continue
                            if not self.oneCharDiff(curr,nei):
                                continue
                            visited.add(nei)
                            q.append(nei)
            
            res = float("inf")
            for word in wordList:
                if self.oneCharDiff(beginWord, word):
                    level = bfs(word)
                    if level:
                        res = min(res,level)

            return 0 if res == float("inf") else res

    
    def oneCharDiff(self, w1, w2):
        count = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                count += 1
        
        return True if count == 1 else False

    
            

