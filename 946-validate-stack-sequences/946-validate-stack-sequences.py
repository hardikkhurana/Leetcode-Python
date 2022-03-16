"""
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i,j=0,0
        n=len(pushed)
        m=len(popped)
        visited=set()
        st=[None]
        while True:
            if j==m:
                return True
            if popped[j] in visited and st[-1]!=popped[j]:
                return False
            while st[-1] !=popped[j]:
                st.append(pushed[i])
                visited.add(pushed[i])
                i+=1
            st.pop()
            j+=1
"""        
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st=[]
        j=0
        for i in pushed:
            st.append(i)
            while st and st[-1]==popped[j]:
                j+=1
                st.pop()
        if len(st)==0:
            return True
        return False