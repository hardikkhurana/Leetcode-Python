class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph=[[] for i in range(len(isConnected))]
        n=len(isConnected)
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j]==1:
                    graph[i].append(j)
                    graph[j].append(i)
                    
        stack=[]
        visited=[False]*n
        
        def stackBuilder(d):
            visited[d]=True
            for i in graph[d]:
                if not visited[i]:
                    stackBuilder(i)
            stack.append(d)
            
        for i in range(n):
            if not visited[i]:
                stackBuilder(i)
            
        visited=[False]*n
        
        ans=0
        while stack:
            i=stack.pop()
            if not visited[i]:
                ans+=1
                stackBuilder(i)
        return ans