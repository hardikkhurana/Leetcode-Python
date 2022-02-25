class Solution:
    def myAtoi(self, s: str) -> int:

        res=""
        for i in range(len(s)):
            if s[i]==" ":
                continue
            if s[i].isnumeric():
                while i<len(s) and s[i].isnumeric():
                    res+=s[i]
                    i+=1
                break
            if (s[i]=="-" or s[i]=="+") and i+1<len(s) and s[i+1].isnumeric():
                res+=s[i]
                k=i+1
                while k<len(s) and s[k].isnumeric():
                    res+=s[k]
                    k+=1
                break
            return 0
        if res=="":
            return 0
        res=int(res)
        if res>2**31-1:
            return (2**31)-1
        elif res< -1*(2**31):
            return -1*(2**31)
        else:
            return res
        
        
        
     