class Solution:
    def simplifyPath(self, path: str) -> str:
        st=[]
        i=0
        n=len(path)
        while i<n:
            if path[i]=="/":
                if st and st[-1]=="/":
                    i+=1
                    continue
                st.append("/")
                i+=1
            else:
                temp=""
                while i<n and path[i]!="/":
                    temp+=path[i]
                    i+=1
                if temp==".":
                    continue
                elif temp=="..":
                    if len(st)>1:
                        st.pop()
                        st.pop()
                else:
                    st.append(temp)
        if len(st)>1 and st[-1]=="/":
            st.pop()
        return "".join(st)
                
                