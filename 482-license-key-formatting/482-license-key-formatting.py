class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ss=""
        for i in s:
            if i.isalnum():
                ss+=i.upper()
        left=0
        right=len(ss)-1
        ans=""
        while right>=left:
            for i in range(k):
                if right<0:
                    break
                ans = ss[right] + ans
                right -= 1
            if right>=0:
                ans="-"+ans
        return ans
            