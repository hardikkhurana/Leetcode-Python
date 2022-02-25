class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=0
        mx=""
        for i in range(len(s)):
            left=i-1
            right=i+1
            while left>-1 and right<len(s) and s[left]==s[right]:
                if (right-left)>ans:
                    ans=right-left
                    mx=s[left:right+1]
                left-=1
                right+=1
            
            left=i
            right=i+1
            while left>-1 and right<len(s) and s[left]==s[right]:
                if (right-left)>ans:
                    ans=right-left
                    mx=s[left:right+1]
                left-=1
                right+=1
        if mx=="":
            return s[0]
        return mx
            