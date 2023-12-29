"
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 0

        for k in range(len(s)):
            i,j = k,k
            while i>-1 and j<len(s) and s[i]==s[j]:
                i-=1
                j+=1
        resS = ""
                if j-i+1>res:
                    res = j-i+1
                    resS = s[i:j+1]
            i,j = k,k+1
            while i>-1 and j<len(s) and s[i]==s[j]:
                if j-i+1>res:
                    res = j-i+1
                    resS = s[i:j+1]
                i-=1
                j+=1
        return resS
