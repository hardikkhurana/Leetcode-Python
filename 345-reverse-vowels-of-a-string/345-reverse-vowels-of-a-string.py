class Solution:
    def reverseVowels(self, s: str) -> str:
        st=[]
        v=set(("a","e","i","o","u","A","E","I","O","U"))
        for i in s:
            if i in v:
                st.append(i)
        ans=""
        for i in s:
            if i in v:
                ans+=st.pop()
            else:
                ans+=i
        return ans
            