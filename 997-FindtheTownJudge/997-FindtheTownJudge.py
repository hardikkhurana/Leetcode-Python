class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        tnobody=set([i for i in range(1,n+1)])
        hmap=defaultdict(lambda : set())
        for i,j in trust:
            if i in tnobody:
                tnobody.remove(i)
            hmap[j].add(i)
        if len(tnobody)!=1:
            return -1
        j=tnobody.pop()
        print(j)
        if len(hmap[j])!=n-1:
            return -1
        return j
2
