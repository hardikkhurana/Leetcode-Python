#User function Template for python3
from collections import defaultdict
class Solution:
    
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        stack=[]
        visited=[False] * V

        transpose=[[] for i in range(V)]
        for i in range(V):
            for j in adj[i]:
                transpose[j].append(i)
                
        
        def stackBuilder(d):
            visited[d] = True
            for i in adj[d]:
                if not visited[i]:
                    stackBuilder(i)
            stack.append(d)
    
    
        for i in range(V):
            if not visited[i]:
                stackBuilder(i)
   
        
        visited=[False] * V
        
        def dfs(d):
            visited[d] = True
            for i in transpose[d]:
                if not visited[i]:
                    dfs(i)
        ans=0
        while stack:
            i=stack.pop()
            if not visited[i]:
                ans+=1
                dfs(i)
                
        return ans
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import OrderedDict 
import sys 

sys.setrecursionlimit(10**6) 
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        print(ob.kosaraju(V, adj))
# } Driver Code Ends