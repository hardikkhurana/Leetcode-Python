import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left=0
        right=0
        res=[]
        q=collections.deque() #index
        
        while right<len(nums):
            while q and nums[q[-1]]<nums[right]:
                q.pop()
            q.append(right)
            if left>q[0]:
                q.popleft()
            if (right+1)>=k:
                res.append(nums[q[0]])
                left+=1
            right+=1
        return res
"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        nextgreater=[-1 for i in range(len(nums))]
        stack=[]
        for i,a in enumerate(nums):
            while stack and nums[stack[-1]]<a:
                nextgreater[stack.pop()]=i
            stack.append(i)
        res=[]
        start=0
        end=k
        for i in range(len(nums)-k+1):
            maxele_pos=nextgreater[i]
            prev=i
            while maxele_pos>=start and maxele_pos<end:
                prev=maxele_pos
                maxele_pos=nextgreater[maxele_pos]
            res.append(nums[prev])
            start+=1
            end+=1
        return res
"""            
            
            
                
            
        
            