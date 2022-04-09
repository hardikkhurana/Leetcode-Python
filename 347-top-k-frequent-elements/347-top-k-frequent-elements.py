"""class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        nums=[]
        for i,e in c.items():
            nums.append([i,e])
        nums.sort(reverse=True,key=itemgetter(1))
        res=[]
        for i in range(k):
            res.append(nums[i][0])            
        return res
"""            
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        nums=[[] for i in range(len(nums)+1)]
        for i,e in c.items():
            nums[e].append(i)
        res=[]
        for i in range(len(nums)):
            if k==0:
                return res
            if nums[-1]:
                while nums[-1]:
                    res.append(nums[-1][-1])
                    nums[-1].pop()
                    k=k-1
                    if k==0:
                        return res
            nums.pop()
            
        
        