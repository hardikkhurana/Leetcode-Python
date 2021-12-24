class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        rb,lb=[len(heights) for i in range(len(heights)) ],[-1 for i in range(len(heights))]
        stack=[]
        for i,a in enumerate(heights):
            while stack and heights[stack[-1]]>a:
                rb[stack.pop()]=i
            stack.append(i)        
        stack=[]
        for i in range(len(heights)-1,-1,-1):
            while stack and heights[stack[-1]]>heights[i]:
                lb[stack.pop()]=i
            stack.append(i)
        maxarea=0
        for i in range(len(heights)):
            width=rb[i]-lb[i]-1
            area=width*heights[i]
            maxarea=max(maxarea,area)            
        return maxarea
        