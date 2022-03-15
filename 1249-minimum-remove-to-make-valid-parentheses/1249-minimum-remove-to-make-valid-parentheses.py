class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        c=set()
        o=[]
        for i in range(len(s)):
            if s[i]=="(":
                o.append(i)
            elif s[i]==")":
                if o:
                    o.pop()
                else:
                    c.add(i)
        o=set(o)
        res=""
        for i in range(len(s)):
            if i not in c and i not in o:
                res+=s[i]
        return res