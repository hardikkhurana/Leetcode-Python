class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        def main(a,b,fn):
            if fn=="-":
                return a-b
            elif fn=="+":
                return a+b
            elif fn=="*":
                return a*b
            else:
                return int(a/b)
            
        st=[]
        for i in tokens:
            if i.isnumeric() or len(i)>1:
                st.append(int(i))
            else:
                a=st.pop()
                b=st.pop()
                st.append(main(b,a,i))
        return st[0]
                
        