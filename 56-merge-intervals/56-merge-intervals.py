class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res=[]
        intervals.sort()
        p=0
        while p<len(intervals):
            start=intervals[p][0]
            end=intervals[p][1]
            k=p+1
            while k<len(intervals) and intervals[k][0]<=end:
                end =max(end,intervals[k][1])
                k+=1
            res.append([start,end])
            p=k
        return res
        