class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for i in s:
            if i=="]":
                st=""
                while stack[-1]!="[":
                    j=stack.pop()
                    st=j+st
                stack.pop()
                n=""
                while stack[-1].isnumeric():
                    k=stack.pop()
                    n=k+n
                    if len(stack)==0:
                        break
                stack.append(st*int(n))
            else:
                stack.append(i)
        return ("".join(stack))