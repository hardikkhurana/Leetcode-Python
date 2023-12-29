"
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        res=0
        st=set()
        for r,c in enumerate(s):
            while c in st:
                st.remove(s[l])
                l+=1
            st.add(c)
            res = max(res,r-l+1)
        return res
