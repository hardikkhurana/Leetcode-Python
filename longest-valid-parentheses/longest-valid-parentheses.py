class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res=0
        st=[-1]
        for i in range(len(s)):
            if s[i]=="(":
                st.append(i)
            else:
                st.pop()
                if len(st)!=0:
                    res=max(res,i-st[-1])
                else:
                    st.append(i)
        return res
                    
        