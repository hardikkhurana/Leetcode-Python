class Solution:
    def candy(self, ratings: List[int]) -> int:
        dp=[1 for i in range(len(ratings))]
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                dp[i]=dp[i-1]+1
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                if dp[i]<=dp[i+1]:
                    dp[i]=dp[i+1]+1
                    
        return sum(dp)
        