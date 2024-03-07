class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = defaultdict(list)

        for word in strs:
            h[tuple(sorted(word))].append(word)
        
        return h.values()
["eat","tea","tan","ate","nat","bat"]
