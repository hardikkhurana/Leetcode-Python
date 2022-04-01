"""
        Do not return anything, modify s in-place instead.
        """

class Solution:
    def reverseString(self, s: List[str]) -> None:
        i,j = 0,len(s)-1
        while i<j:
            s[i],s[j] = s[j],s[i]
            i += 1
            j -= 1
