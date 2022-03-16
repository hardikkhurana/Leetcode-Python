class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i=0
        j=0
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
        