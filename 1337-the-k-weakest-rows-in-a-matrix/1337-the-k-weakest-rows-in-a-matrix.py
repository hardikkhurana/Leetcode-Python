import heapq
from collections import deque
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        minheap=[]
        d=defaultdict(deque)
        for i in range(len(mat)):
            d[mat[i].count(1)].append(i)
        i=0
        res=[]
        while k and i<101:
            while i in d and len(d[i])>0 and k:
                res.append(d[i][0])
                d[i].popleft()
                k-=1
            i+=1
        return res