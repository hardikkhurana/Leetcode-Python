class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
    
        for t in tokens:
            if t == "+":
                a = st.pop()
                b = st.pop()
                st.append(a+b)
            elif t == "*":
                a = st.pop()
                b = st.pop()
                st.append(a*b)
            elif t == "-":
                a = st.pop()
                b = st.pop()
                st.append(b-a)
            elif t == "/":
                a = st.pop()
                b = st.pop()
                st.append(int(b/a))
            else:
                st.append(int(t))
        print(st)
        return st[0]
