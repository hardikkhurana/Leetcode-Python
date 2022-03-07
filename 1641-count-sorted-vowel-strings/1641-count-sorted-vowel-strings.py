"""
class Solution:
    def countVowelStrings(self, n: int) -> int:
        s=["u","o","i","e","a"]
        l=["a","e","i","o","u"]
        for _ in range(1,n):
            tmp=[]
            for j in l:
                for k in s:
                    if k>=j[0]:
                        tmp.append(k+j)
                    else:
                        break
            l=tmp
        return len(l)
"""
class Solution:
    def countVowelStrings(self, n: int) -> int:
        l=[1,1,1,1,1]
        for _ in range(1,n):
            for j in range(4):
                l[j]=sum(l[j:])
        return sum(l)
        