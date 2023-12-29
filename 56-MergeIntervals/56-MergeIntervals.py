[
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=[intervals[0]]
        for i,j in intervals[1:]:
            if res[-1][1]<i:
                res.append([i,j])
            else:
                res[-1][1]=max(res[-1][1],j)
        return res
