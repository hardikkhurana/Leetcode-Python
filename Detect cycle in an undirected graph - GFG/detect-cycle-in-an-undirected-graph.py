class Solution:
    
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V, adj):
	    
	    
	    def dfs(ele,visit,parent):
	        visit[ele]=True
	        for i in adj[ele]:
	            if visit[i]==False:
	                if dfs(i,visit,ele):
	                    return True
	            elif parent!=i:
	                return True
	        return False
	   
	    visit=[False for i in range(V)]    
	    for i in range(V):
	        if visit[i]==False:
	            if dfs(i,visit,-1)==True:
	                return True
	    return False
	        
	        

#{ 
#  Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends