#User function Template for python3


class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        
        def dfs(ele,visit,recStack):
	        visit[ele]=True
	        recStack[ele]=True
	        for i in adj[ele]:
	            if visit[i]==False:
	                if dfs(i,visit,recStack):
	                    return True
	            elif recStack[i]==True:
	                return True
	        recStack[ele]=False
	        return False
	   
	    visit=[False for i in range(V+1)]
	    recStack=[False for i in range(V+1)]
	    for i in range(V):
	        if visit[i]==False:
	            if dfs(i,visit,recStack)==True:
	                return True
	    return False
	        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

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
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends