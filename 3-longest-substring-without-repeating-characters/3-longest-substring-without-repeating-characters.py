class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h=[0]*128
        left=0
        right=0
        ans=0
        while right<len(s):
            o=ord(s[right])
            if h[o]==0:
                h[o]=1
                right+=1
            else:
                h[ord(s[left])]-=1
                left+=1
            ans=max(ans,right-left)
        return ans