class Solution:
    def calculate(self, s: str) -> int:
        
        def update(sign,num,stack):
            if sign=="+":
                stack.append(num)
            if sign=="-":
                stack.append(-num)
            if sign=="*":
                stack.append(stack.pop()*num)
            if sign=="/":
                stack.append(int(stack.pop()/num))
            return stack
        
        def solve(i,s):
            stack,num,sign=[],0,"+"
            while i<len(s):
                if s[i].isdigit():
                    num=num*10 + int(s[i])
                elif s[i] in ["+","-","/","*"]:
                    stack=update(sign,num,stack)
                    num,sign=0,s[i]
                elif s[i]=="(":
                    num,sign=solve(i+1,s)
                elif s[i]==")":
                    stack=update(sign,num,stack)
                    return sum(stack),i
                i+=1
            stack=update(sign,num,stack)
            return sum(stack)
        
        return solve(0,s)