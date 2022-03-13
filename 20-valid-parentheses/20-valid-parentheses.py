class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        l=["[","(","{"]
        a=set(l)
        for i in s:
            if i in a:
                st.append(i)
            else:
                if not st:
                    return False
                if i=="]" and st[-1]=="[":
                    st.pop()
                elif i=="}"and st[-1]=="{":
                    st.pop()
                elif i==")"and st[-1]=="(":
                    st.pop()
                else:
                    return False
        if not st:
            return True
                    
            
        
        