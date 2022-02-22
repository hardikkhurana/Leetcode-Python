import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap=[]
        for i in nums:
            if len(minheap)==k:
                heapq.heappush(minheap,i)
                heapq.heappop(minheap)
            else:
                heapq.heappush(minheap,i) 
        return heapq.heappop(minheap)