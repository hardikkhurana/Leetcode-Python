[
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        h = [[-j,i] for i,j in c.items()]
        heapq.heapify(h)
        res=[]
        for _ in range(k):
            j,i=heapq.heappop(h)
            res.append(i)
        return res
