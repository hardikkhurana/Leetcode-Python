#-96
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res=""
        while n!=0:
            n-=1
            ans=k-n
            if ans>26:
                k-=26
                res+="z"
            else:
                res+=chr(ans+96)
                k-=ans
        return res[::-1]
            