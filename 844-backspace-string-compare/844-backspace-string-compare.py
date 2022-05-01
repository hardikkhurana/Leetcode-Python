class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st,tt="",""
        back=0
        for i in range(len(s)-1,-1,-1):
            if s[i]=="#":
                back+=1
            else:
                if back:
                    back-=1
                else:
                    st=s[i]+st
        back=0
        for i in range(len(t)-1,-1,-1):
            if t[i]=="#":
                back+=1
            else:
                if back:
                    back-=1
                else:
                    tt=t[i]+tt
        return st==tt
                
        