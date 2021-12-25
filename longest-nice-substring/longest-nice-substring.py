class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s)<2:
            return ""
        uset=set()
        for i in range(len(s)):
            uset.add(s[i])
        for i in range(len(s)):
            if s[i].lower() in uset and s[i].upper() in uset:
                continue
            prev= self.longestNiceSubstring(s[:i])
            next= self.longestNiceSubstring(s[i+1:])
            if len(prev)>=len(next):
                return prev
            else:
                return next
        return s