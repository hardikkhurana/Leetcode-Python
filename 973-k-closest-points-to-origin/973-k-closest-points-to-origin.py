class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for i,j in points:
            heapq.heappush(heap,((-((i**2+j**2)**1/2),i,j)))
            if len(heap)>k:
                heapq.heappop(heap)
        res=[]
        for a,b,c in heap:
            res.append([b,c])
        return res