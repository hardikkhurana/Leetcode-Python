"
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        
        def pali(a):
            return a==a[::-1]

        def helper(ind,curr):
            if ind==len(s):
                res.append(curr.copy())
                return
            for j in range(ind,len(s)):
                if pali(s[ind:j+1]):
                    curr.append(s[ind:j+1])
                    helper(j+1,curr)
                    curr.pop()
        helper(0,[])
        return res
