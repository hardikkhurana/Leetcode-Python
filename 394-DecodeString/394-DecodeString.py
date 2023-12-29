"
class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        for ch in s:
            if ch!="]":
                st.append(ch)
            else:
                tmp=""
                while st and st[-1].isalpha():
                    tmp = st.pop()+tmp
                n=""
                while st and st[-1].isnumeric():
                    n=st.pop()+n
                if n:
                    st.append(int(n)*tmp)
                else:
                    st.append(tmp)
        print(st)
                st.pop()
        return "".join(st)
