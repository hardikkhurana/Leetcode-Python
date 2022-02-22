class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        d={alpha[i]:i+1 for i in range(len(alpha))}
        n=len(columnTitle)-1
        ans=0
        for i in columnTitle:
            ans+=((26**n)*d[i])
            n-=1
        return ans
            