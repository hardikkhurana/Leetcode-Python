[
class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        st=[]
        res=[0 for i in range(len(temp))]
        for i,t in enumerate(temp):
            while st and st[-1][0]<t:
                a,b=st.pop()
                res[b] = i-b
            st.append([t,i])
        return res
