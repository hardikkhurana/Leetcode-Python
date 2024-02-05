class Solution:
    def firstUniqChar(self, s: str) -> int:
        count=Counter(s)
        for i,c in enumerate(s):
            if count[c] == 1:
                return i
        return -1
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        st=set()
        h={ c:i for i,c in enumerate(s) }

        for i,c in enumerate(s):
            if h[c]==i and c not in st:
                return i
            st.add(c)
        return -1
"""
