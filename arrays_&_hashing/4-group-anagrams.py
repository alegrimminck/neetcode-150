class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for s in strs:
            key = [0] * 26
            for char in s:
                key[ord(char) - ord("a")] += 1
            hashMap[tuple(key)].append(s)
        return hashMap.values()
        
