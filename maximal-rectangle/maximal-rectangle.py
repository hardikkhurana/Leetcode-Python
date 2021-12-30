class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        def largestRectangleArea(heights):
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
                maxarea=max(maxarea,int(area))            
            return maxarea
        
        max_=0
        for i in range(len(matrix)):
            if i==0:
                temp=list(map(int,matrix[i]))
            else:
                for j in range(len(matrix[0])):
                    if matrix[i][j]!="0":
                        temp[j]+=int(matrix[i][j])
                    else:
                        temp[j]=0
            print(temp)
            max_=max(max_,largestRectangleArea(temp))
        return max_
        
        
