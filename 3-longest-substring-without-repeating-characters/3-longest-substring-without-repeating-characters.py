class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        contains=set()
        res=0
        i,j=0,0
        while j<len(s):
            if s[j] not in contains:
                contains.add(s[j])
                j+=1
            else:
                contains.remove(s[i])
                i+=1
            res=max(res,j-i)
        return res