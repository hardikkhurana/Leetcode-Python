class Solution:
    def numSplits(self, s: str) -> int:
        l,r=[],[0 for i in range(len(s))]
        h=set()
        for i in range(len(s)):
            h.add(s[i])
            l.append(len(h))
        h=set()
        ans=0
        for i in range(len(s)-1,-1,-1):
            r[i]=len(h)
            h.add(s[i])
            if r[i]==l[i]:
                ans+=1
                
        return ans
        