class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1=(sorted(s1))
        s2=(sorted(s2))
        
        def check(a,b):
            for i in range(len(a)):
                if a[i]>b[i]:
                    return False 
            return True
        
        return check(s1,s2) or check(s2,s1)
        
        