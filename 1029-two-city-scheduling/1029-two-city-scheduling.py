class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff=[(c2-c1,c1,c2) for c1,c2 in costs]
        diff.sort()
        res=0
        n=len(diff)//2
        for i in range(len(diff)):
            if i<n:
                res+=diff[i][2]
            else:
                res+=diff[i][1]
        return res
            
            