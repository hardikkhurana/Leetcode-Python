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
            
        
        