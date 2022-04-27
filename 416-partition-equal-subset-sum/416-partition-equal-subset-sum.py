"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        l=[False]
        s=sum(nums)
        if s%2!=0:
            return False
        target=s//2
        n=len(nums)
        def helper(index,total):
            if total==target:
                l[0]=True
                print(total,target)
                return
            if total>target or index>=n:
                return
            helper(index+1,total+nums[index])
            helper(index+1,total)
        helper(0,0)
        return l[0]
"""
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s=sum(nums)
        if s%2!=0:
            return False
        target=s//2
        dp=set([0])
        for i in range(len(nums)-1,-1,-1):
            tempdp=set()
            for j in dp:
                tmp=j+nums[i]
                if tmp==target:
                    return True
                tempdp.add(tmp)
                tempdp.add(j)
            dp=tempdp
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s=sum(nums)
        if s%2!=0:
            return False
        target=s//2
        dp=[[True]*(len(nums)+1) for j in range(target+1)]
        for i in range(1,target+1):
            dp[i][0]=False
        for i in range(1,target+1):
            for j in range(1,len(nums)+1):
                dp[i][j]=dp[i][j-1]
                if i>=nums[j-1]:
                    dp[i][j]=dp[i][j] or dp[i-nums[j-1]][j-1]
                    
        return dp[-1][-1]
        
            
        
        
        
        
        
