class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i=0
        res=[]
        while i<len(intervals) and intervals[i][0]<newInterval[0]:
            res.append(intervals[i])
            i+=1
        if res and res[-1][0]<=newInterval[0]<=res[-1][1]:
            res[-1][1]=max(res[-1][1],newInterval[1])
        else:
            res.append(newInterval)
        for i in intervals[i:]:
            if res[-1][0]<=i[0]<=res[-1][1]:
                res[-1][1]=max(res[-1][1],i[1])
            else:
                res.append(i)
        return res
            
    
        
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        stack=[]
        stack.append(intervals[0])
        for i in intervals[1:]:
            if stack[-1][0]<=i[0]<=stack[-1][1]:
                stack[-1][1]=max(stack[-1][1],i[1])
            else:
                stack.append(i)
                
        return stack
        """