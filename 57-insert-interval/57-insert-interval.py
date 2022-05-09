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
        