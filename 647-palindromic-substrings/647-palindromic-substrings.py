class Solution:
    def countSubstrings(self, s: str) -> int:
        res=0
        for k in range(len(s)):
            res+=1
            i,j=k-1,k+1
            while i>=0 and j<len(s) and s[i]==s[j]:
                res+=1
                i-=1
                j+=1
            i,j=k,k+1
            while i>=0 and j<len(s) and s[i]==s[j]:
                res+=1
                i-=1
                j+=1
        return res
            
        