class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans=0
        o=[]
        for i in range(len(s)):
            if s[i]=="(":
                o.append(i)
            if s[i]==")":
                temp=o.pop()
                if type(temp) is list:
                    o.pop()
                    o.append([temp[0]*2])
                else:
                    o.append([1])   
                if len(o)>1 and type(o[-1]) is list and type(o[-2]) is list:
                    t1=o.pop()
                    t2=o.pop()
                    o.append([t1[0]+t2[0]])
            if len(o)==1 and type(o[0]) is list:
                ans+=o.pop()[0]
        return ans
            