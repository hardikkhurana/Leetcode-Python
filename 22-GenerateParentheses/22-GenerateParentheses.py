3
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def helper(i,j,curr):
            if i==n and j==n:
                res.append(curr)
                helper(i+1,j,curr+"(")
            if j+1<=n and j+1<=i:
                helper(i,j+1,curr+")")
        helper(0,0,"")
        res=[]
                return
            if i+1<=n:
        return res
