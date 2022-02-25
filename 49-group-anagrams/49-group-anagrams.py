class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h=defaultdict(list)
        for i in strs:
            count=[0]*26
            for j in i:
                count[ord(j)-ord("a")]+=1
            h[tuple(count)].append(i)
        return [h[i] for i in h]
                
        