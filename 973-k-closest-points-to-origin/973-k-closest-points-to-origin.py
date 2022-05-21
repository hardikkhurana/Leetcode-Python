class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for i,j in points:
            heap.append((-((i**2+j**2)**1/2),i,j))
        heapq.heapify(heap)
        while len(heap)>k:
            heapq.heappop(heap)
        res=[]
        for a,b,c in heap:
            res.append([b,c])
        return res